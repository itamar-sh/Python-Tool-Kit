import pytest
from string_functions.stream_handling.conversion_handling import parse_conversation  # Replace 'your_module' with the actual name of your module

def test_basic_conversation():
    text = """out: Is this Brad?
in: No, this is Brent"""
    
    expected_output = [
        {"time": 0, "direction": "out", "text": "Is this Brad?"},
        {"time": 5, "direction": "in", "text": "No, this is Brent"}
    ]
    
    assert parse_conversation(text) == expected_output

def test_time_skip():
    text = """out: Is this Brad?
in: No, this is Brent
[skip 150 seconds]
out: The person in charge of the Hot-as-Heck-Chili Cook Off this year?"""
    
    expected_output = [
        {"time": 0, "direction": "out", "text": "Is this Brad?"},
        {"time": 5, "direction": "in", "text": "No, this is Brent"},
        {"time": 155, "direction": "out", "text": "The person in charge of the Hot-as-Heck-Chili Cook Off this year?"}
    ]
    
    assert parse_conversation(text) == expected_output

def test_time_skip_in_row():
    text = """out: Is this Brad?
in: No, this is Brent
[skip 150 seconds]
[skip 150 seconds]
[skip 150 seconds]
out: The person in charge of the Hot-as-Heck-Chili Cook Off this year?"""
    
    expected_output = [
        {"time": 0, "direction": "out", "text": "Is this Brad?"},
        {"time": 5, "direction": "in", "text": "No, this is Brent"},
        {"time": 455, "direction": "out", "text": "The person in charge of the Hot-as-Heck-Chili Cook Off this year?"}
    ]
    
    assert parse_conversation(text) == expected_output


def test_time_skip__zero_in_row():
    text = """out: Is this Brad?
in: No, this is Brent
[skip 0 seconds]
[skip 0 seconds]
[skip 0 seconds]
out: The person in charge of the Hot-as-Heck-Chili Cook Off this year?"""
    
    expected_output = [
        {"time": 0, "direction": "out", "text": "Is this Brad?"},
        {"time": 5, "direction": "in", "text": "No, this is Brent"},
        {"time": 5, "direction": "out", "text": "The person in charge of the Hot-as-Heck-Chili Cook Off this year?"}
    ]
    
    assert parse_conversation(text) == expected_output

def test_message_with_tags():
    text = """in: <highlight, copy>Yes, Martin"""
    
    expected_output = [
        {"time": 0, "direction": "in", "text": "Yes, Martin", "highlight": True, "copy": True}
    ]
    
    assert parse_conversation(text) == expected_output

def test_combined():
    text = """out: Is this Brad?
in: No, this is Brent
[skip 20 seconds]
out: The person in charge of the Hot-as-Heck-Chili Cook Off this year?
in: <highlight, copy>Yes, Martin
in: We talk very often :)
in: And I've hosted it for the last 13 years
out: Mhmm I'm sure
out: Anyway... Before I was rudely interrupted, I was going to say that I have a question"""
    
    expected_output = [
        {"time": 0, "direction": "out", "text": "Is this Brad?"},
        {"time": 5, "direction": "in", "text": "No, this is Brent"},
        {"time": 25, "direction": "out", "text": "The person in charge of the Hot-as-Heck-Chili Cook Off this year?"},
        {"time": 30, "direction": "in", "text": "Yes, Martin", "highlight": True, "copy": True},
        {"time": 35, "direction": "in", "text": "We talk very often :)"},
        {"time": 40, "direction": "in", "text": "And I've hosted it for the last 13 years"},
        {"time": 45, "direction": "out", "text": "Mhmm I'm sure"},
        {"time": 50, "direction": "out", "text": "Anyway... Before I was rudely interrupted, I was going to say that I have a question"}
    ]
    
    assert parse_conversation(text) == expected_output

def test_empty_lines():
    text = """out: Is this Brad?
    
in: No, this is Brent"""
    
    expected_output = [
        {"time": 0, "direction": "out", "text": "Is this Brad?"},
        {"time": 5, "direction": "in", "text": "No, this is Brent"}
    ]
    
    assert parse_conversation(text) == expected_output

def test_only_skip():
    text = """[skip 20 seconds]"""
    
    expected_output = []
    
    assert parse_conversation(text) == expected_output

def test_negative_time_skip():
    text = """out: Is this Brad?
in: No, this is Brent
[skip -10 seconds]
out: The person in charge of the Hot-as-Heck-Chili Cook Off this year?"""
    
    expected_output = [
        {"time": 0, "direction": "out", "text": "Is this Brad?"},
        {"time": 5, "direction": "in", "text": "No, this is Brent"},
        {"time": -5, "direction": "out", "text": "The person in charge of the Hot-as-Heck-Chili Cook Off this year?"}
    ]
    
    assert parse_conversation(text) == expected_output


def test_message_with_nested_brackets():
    text = """in: <highlight>Yes, <Martin>"""
    
    expected_output = [
        {"time": 0, "direction": "in", "text": "Yes, <Martin>", "highlight": True}
    ]
    
    assert parse_conversation(text) == expected_output


def test_message_with_invalid_tag_format():
    text = """in: <highlight,copy Yes, Martin"""
    
    expected_output = [
        {"time": 0, "direction": "in", "text": "<highlight,copy Yes, Martin"}
    ]
    
    assert parse_conversation(text) == expected_output


def test_message_with_spaces_in_tags():
    text = """in: <highlight, needs review>Yes, Martin"""
    
    expected_output = [
        {"time": 0, "direction": "in", "text": "Yes, Martin", "highlight": True, "needs review": True}
    ]
    
    assert parse_conversation(text) == expected_output


# def test_invalid_time_skip_format():
#     text = """out: Is this Brad?
# in: No, this is Brent
# [skip seconds]
# out: The person in charge of the Hot-as-Heck-Chili Cook Off this year?"""
    
#     expected_output = [
#         {"time": 0, "direction": "out", "text": "Is this Brad?"},
#         {"time": 5, "direction": "in", "text": "No, this is Brent"},
#         {"time": 10, "direction": "out", "text": "The person in charge of the Hot-as-Heck-Chili Cook Off this year?"}
#     ]
    
#     assert parse_conversation(text) == expected_output

def test_complex_conversation_with_skips_and_tags():
    text = """out: Is this Brad?
in: No, this is Brent
out: Oh, sorry. I thought it was Brad.
[skip 45 seconds]
in: <highlight>It's okay, happens all the time
out: <urgent>Are you still coming to the meeting at 3 PM?
in: Yes, I'll be there
[skip 15 seconds]
out: Don't forget to bring the documents.
in: Of course, I have them ready
out: Great, see you then
[skip 30 seconds]
in: <reminder,important>Remember to review the budget report before the meeting
out: Got it, thanks for the reminder
in: Anytime!
[skip 10 seconds]
out: By the way, did you check the new project proposal?
in: Not yet, but I'll get to it soon
out: <priority>It's really important, please do it ASAP
in: Will do, thanks for the heads-up"""

    expected_output = [
        {"time": 0, "direction": "out", "text": "Is this Brad?"},
        {"time": 5, "direction": "in", "text": "No, this is Brent"},
        {"time": 10, "direction": "out", "text": "Oh, sorry. I thought it was Brad."},
        {"time": 55, "direction": "in", "text": "It's okay, happens all the time", "highlight": True},
        {"time": 60, "direction": "out", "text": "Are you still coming to the meeting at 3 PM?", "urgent": True},
        {"time": 65, "direction": "in", "text": "Yes, I'll be there"},
        {"time": 80, "direction": "out", "text": "Don't forget to bring the documents."},
        {"time": 85, "direction": "in", "text": "Of course, I have them ready"},
        {"time": 90, "direction": "out", "text": "Great, see you then"},
        {"time": 120, "direction": "in", "text": "Remember to review the budget report before the meeting", "reminder": True, "important": True},
        {"time": 125, "direction": "out", "text": "Got it, thanks for the reminder"},
        {"time": 130, "direction": "in", "text": "Anytime!"},
        {"time": 140, "direction": "out", "text": "By the way, did you check the new project proposal?"},
        {"time": 145, "direction": "in", "text": "Not yet, but I'll get to it soon"},
        {"time": 150, "direction": "out", "text": "It's really important, please do it ASAP", "priority": True},
        {"time": 155, "direction": "in", "text": "Will do, thanks for the heads-up"}
    ]
    
    assert parse_conversation(text) == expected_output

def test_mixed_messages_with_various_tags_and_skips():
    text = """out: Hello, can we discuss the project update?
in: Sure, let me pull up the documents
[skip 60 seconds]
in: <urgent,review>Okay, I have the documents now
out: Great, let's start with the first section
[skip       5 seconds]
in: The first section covers the overview of the project
out: Yes, I have some questions about it
in: Go ahead
[skip 10      seconds]
out: First, can you explain the budget allocation?
in: <detailed>We've allocated funds based on the priority tasks
out: Can you provide more details on the priority tasks?
in: Yes, the priority tasks are listed in section 2
out: Thanks, I'll check it out
[skip 20 seconds]
in: <highlight>Also, don't forget to check the risk assessment
out: Sure, I'll review that next
in: Great, let's move on to the timeline
out: Yes, let's do that
[skip 30 seconds]
in: The timeline is crucial for tracking our milestones
out: I agree, let's ensure we meet all the deadlines
in: Absolutely, I'll keep you updated on the progress"""

    expected_output = [
        {"time": 0, "direction": "out", "text": "Hello, can we discuss the project update?"},
        {"time": 5, "direction": "in", "text": "Sure, let me pull up the documents"},
        {"time": 65, "direction": "in", "text": "Okay, I have the documents now", "urgent": True, "review": True},
        {"time": 70, "direction": "out", "text": "Great, let's start with the first section"},
        {"time": 75, "direction": "in", "text": "The first section covers the overview of the project"},
        {"time": 80, "direction": "out", "text": "Yes, I have some questions about it"},
        {"time": 85, "direction": "in", "text": "Go ahead"},
        {"time": 95, "direction": "out", "text": "First, can you explain the budget allocation?"},
        {"time": 100, "direction": "in", "text": "We've allocated funds based on the priority tasks", "detailed": True},
        {"time": 105, "direction": "out", "text": "Can you provide more details on the priority tasks?"},
        {"time": 110, "direction": "in", "text": "Yes, the priority tasks are listed in section 2"},
        {"time": 115, "direction": "out", "text": "Thanks, I'll check it out"},
        {"time": 135, "direction": "in", "text": "Also, don't forget to check the risk assessment", "highlight": True},
        {"time": 140, "direction": "out", "text": "Sure, I'll review that next"},
        {"time": 145, "direction": "in", "text": "Great, let's move on to the timeline"},
        {"time": 150, "direction": "out", "text": "Yes, let's do that"},
        {"time": 180, "direction": "in", "text": "The timeline is crucial for tracking our milestones"},
        {"time": 185, "direction": "out", "text": "I agree, let's ensure we meet all the deadlines"},
        {"time": 190, "direction": "in", "text": "Absolutely, I'll keep you updated on the progress"}
    ]
    
    assert parse_conversation(text) == expected_output
