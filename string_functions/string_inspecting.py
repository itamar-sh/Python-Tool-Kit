from typing import List


class StringInspecting:
    def is_palindrome(self, text: str):
        return text[:len(text)//2] == text[-1:len(text)//2:-1]

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