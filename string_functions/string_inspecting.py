from typing import List


class StringInspecting:
    def is_palindrome(self, text: str):
        for i in range(len(text)):
            if text[i] != text[~i]:
                return False
        return True

    def is_palindrome_without_alnum(self, text: str):
        """
        A phrase is a palindrome if, after converting all uppercase letters
        into lowercase letters and removing all non-alphanumeric characters,
        it reads the same forward and backward. Alphanumeric characters
        include letters and numbers.
        """
        text = text.lower()
        left_index = 0
        right_index = len(text)-1
        while left_index < right_index:
            if not text[left_index].isalnum():
                left_index += 1
                continue

            if not text[right_index].isalnum():
                right_index -= 1
                continue

            if text[left_index] != text[right_index]:
                return False

            left_index += 1
            right_index -= 1
        return True

    def get_longest_palindrome_substring(self, text: str):
        """
        Problem:
        Given a string s, return the longest palindromic substring in s.
        Solution:
        Dynamic_table with two pointers - right and center.
        Each stage we conclude from right if we reached this point on other
        checks so every cell is checked less times.

        """
        if len(text) <= 1:
            return text

        max_len = 0
        max_str = ""
        # ensure that all palindromic substrings have an odd length - "bb" will become "#b#b#"
        text_modified = "#" + "#".join(text) + "#"
        # dynamic table which stores the lenghtes of palindromic substrings centered for each char
        dynamic_table = [0 for _ in range(len(text_modified))]
        # center and rightmost point of the substring
        center = 0
        right = 0
        # calculate the longest for each char
        for i in range(len(text_modified)):
            # mirror index is the index of the char that is on the other side of the center.
            # For example. center = 5, i = 6 than the mirror is 4.
            mirror_index = (2 * center) - i
            if i < right:
                # since we smaller than 'right' we already know the limits of our known result.
                dynamic_table[i] = min(right - i, dynamic_table[mirror_index])
            # expand via center of current char
            cond_for_left_boundary = lambda: i - dynamic_table[i] - 1 >= 0
            cond_for_right_boundary = lambda: i + dynamic_table[i] + 1 < len(text_modified)
            cond_for_palindrome_correctness = lambda: text_modified[i-dynamic_table[i]-1] == text_modified[i+dynamic_table[i]+1]
            while cond_for_left_boundary() and cond_for_right_boundary() and cond_for_palindrome_correctness():
                dynamic_table[i] += 1
            # update center and right
            if i + dynamic_table[i] > right:
                center = i
                right = i + dynamic_table[i]
            # update result
            if dynamic_table[i] > max_len:
                max_len = dynamic_table[i]
                max_str = text_modified[i-dynamic_table[i]:i+dynamic_table[i]+1].replace("#", "")
        return max_str

    def get_all_partitions(self, text: str) -> List[List]:
        all_partitions = []
        for partition_index in range(len(text)):
            all_partitions.append([self.get_all_partitions[text[:partition_index]] + self.get_all_partitions[text[partition_index:]]])
        return all_partitions

    def get_palindrom_partitioning(self, text: str) -> List[List]:
        """
        Given a string s, partition s such that every substring of the
        partition is a palindrome. Return all possible palindrome
        partitioning of s.
        """
        pass

    def get_longest_substring_without_duplicates(self, text: str) -> str:
        """
        Given a string s, find the length of the longest substring without
        repeating characters.
        - The implementation uses two pointers approach.
        """
        start = 0
        end = 0
        max_size = 0
        current_word = set()

        while end < len(text):
            if text[end] in current_word:
                max_size = max(max_size, end - start)
                current_word.remove(text[start])
                start += 1
            else:
                current_word.add(text[end])
                end += 1
        return max(max_size, end - start)

    def string_to_int_atoi(self, text):
        MAX_INT = 0x7fffffff
        MIN_INT = ~MAX_INT

        modified_text = text.lstrip()
        sign = 1
        if modified_text and modified_text[0] == "-":
            sign = -1
            modified_text = modified_text[1:]
        elif modified_text and modified_text[0] == "+":
            modified_text = modified_text[1:]

        result = 0
        for char in modified_text:
            # ignore opening zeros
            if char == "0" and result == 0:
                continue

            if not char.isdigit():
                break

            digit = int(char)
            if result > (MAX_INT - digit) // 10:
                return MAX_INT if sign == 1 else MIN_INT
            result = result * 10 + digit
        return result * sign

    def get_longest_common_prefix(self, strs: List[str]) -> List[str]:
        # time complexity: O(m*n)
        common_prefix = [""]
        shortest_str_len = min(len(text) for text in strs)
        for char_index in range(shortest_str_len):
            cur_char = strs[0][char_index]
            if all(text[char_index] == cur_char for text in strs):
                common_prefix.append(cur_char)
            else:
                break
        return "".join(common_prefix)
