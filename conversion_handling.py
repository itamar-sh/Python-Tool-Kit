from typing import List, Dict, Tuple, Any

### CONSTS ###
SKIP_LINE_INDICATOR = "[skip"
SECONDS_TIME_START_INDEX = 6
SECONDS_TIME_END_INDEX = -9
AVAILABLE_DIRECTIONS = ["in:", "out:"]
REGULAR_TIME_BETWEEN_CALLS = 5
OPEN_BOOLEAN_TAG_INDICATOR = "<"
END_BOOLEAN_TAG_INDICATOR = ">"
SEPARATOR_TAGS = ","


def parse_conversation(text: str) -> List[Dict[str, Any]]:
    """
    Parses a conversation string into a list of message dictionaries with timestamps.

    Args:
        text (str): The input conversation string.

    Returns:
        List[Dict[str, Any]]: A list of message dictionaries with 'time', 'direction', and 'text' fields.

    Raises:
        ValueError: If `[skip X seconds]` contains non-numeric or negative value.
        ValueError: If a line lacks a proper direction `("in:" or "out:")` or message content.
    """
    current_time = 0
    result = []
    lines = text.strip().split('\n')
    during_time_skip = True

    for line in lines:
        line_dict, current_time, during_time_skip = handle_line(line, current_time, during_time_skip)
        if line_dict:
            result.append(line_dict)
    return result


def handle_line(line: str, current_time: int, during_time_skip: bool) -> Tuple[Dict[str, Any], int, bool]:
    """
    Handles a single line of the conversation, updating the current time and determining if a time skip occurred.

    Args:
        line (str): A single line from the conversation.
        current_time (int): The current time in seconds.
        during_time_skip (bool): A flag indicating if the last processed line was a time skip.

    Returns:
        Tuple[Dict[str, Any], int, bool]: A tuple containing the message dictionary, updated current time,
        and a flag indicating if a time skip occurred.
    """
    line = line.strip()

    if not line:
        return {}, current_time, during_time_skip

    if is_skip_line(line):
        return handle_skip_line(line, current_time)

    remained_line, direction = extract_direction(line)
    remained_line, tags = extract_tags(remained_line)

    return build_message_dict(current_time, direction, remained_line, tags, during_time_skip)


def is_skip_line(line: str) -> bool:
    """
    Checks if a line is a time skip command.

    Args:
        line (str): A single line from the conversation.

    Returns:
        bool: True if the line is a time skip command, False otherwise.
    """
    return line.startswith(SKIP_LINE_INDICATOR)


def handle_skip_line(line: str, current_time: int) -> Tuple[Dict[str, Any], int, bool]:
    """
    Handles a time skip command line, updating the current time.

    Args:
        line (str): A time skip command line.
        current_time (int): The current time in seconds.

    Returns:
        Tuple[Dict[str, Any], int, bool]: An empty message dictionary, updated current time,
        and a flag indicating a time skip occurred.
    """
    seconds = line[SECONDS_TIME_START_INDEX:SECONDS_TIME_END_INDEX]
    if not seconds.isnumeric:
        raise ValueError(f"Invalid time skip format on line: {line}")
    return {}, current_time + int(seconds), True


def extract_direction(line: str) -> Tuple[str, str]:
    """
    Extracts the message direction and content from a line.

    Args:
        line (str): A single line from the conversation.

    Returns:
        Tuple[str, str]: A tuple containing the message content and direction ('in' or 'out').
    """
    message_content = ""
    direction = ""
    for direction_option in AVAILABLE_DIRECTIONS:
        if line.startswith(direction_option):
            direction = direction_option[:-1]
            message_content = line[len(direction_option):].strip()
    if not message_content:
        raise ValueError(f"A line is not valid - without content. In Line: {line}")
    if not direction:
        raise ValueError(f"A line is not valid - without proper direction from this list: {AVAILABLE_DIRECTIONS}.\n \
                          In Line: {line}")
    return message_content, direction


def extract_tags(message_content: str) -> Tuple[str, List[str]]:
    """
    Extracts tags from the message content.
    In case only on of the openning or closing tags are exists, the tags will
    be considered as part of the message.

    Args:
        message_content (str): The message content with potential tags.

    Returns:
        Tuple[str, List[str]]: A tuple containing the message content without tags and a list of tags.
    """
    tags = []
    if message_content.startswith(OPEN_BOOLEAN_TAG_INDICATOR):
        end_index = message_content.find(END_BOOLEAN_TAG_INDICATOR)
        if end_index != -1:  # there is a matching end indicator
            tags = message_content[1:end_index].split(SEPARATOR_TAGS)
            message_content = message_content[end_index + 1:].strip()
    return message_content, tags


def build_message_dict(current_time: int, direction: str, remained_line: str, tags: List[str], during_time_skip: bool) -> Tuple[Dict[str, Any], int, bool]:
    """
    Builds a message dictionary from the given components.

    Args:
        current_time (int): The current time in seconds.
        direction (str): The message direction ('in' or 'out').
        remained_line (str): The remaining message content.
        tags (List[str]): A list of tags.
        during_time_skip (bool): A flag indicating if the last processed line was a time skip.

    Returns:
        Tuple[Dict[str, Any], int, bool]: A tuple containing the message dictionary, updated current time,
        and a flag indicating if a time skip occurred.
    """
    if not during_time_skip:
        current_time += REGULAR_TIME_BETWEEN_CALLS
    message_dict = {
        'time': current_time,
        'direction': direction,
        'text': remained_line
    }
    for tag in tags:
        message_dict[tag.strip()] = True
    return message_dict, current_time, False
