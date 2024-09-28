from typing import List


class TrieNode:
    def __init__(self):
        self.childs = dict()


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        head = TrieNode()
        max_length = 0
        for num in arr1:
            cur_digit_node = head
            stack_num = []
            while num > 0:
                stack_num.append(num % 10)
                num //= 10
            while stack_num:
                digit = stack_num.pop()
                if digit not in cur_digit_node.childs:
                    cur_digit_node.childs[digit] = TrieNode()
                cur_digit_node = cur_digit_node.childs[digit]

        for num in arr2:
            cur_digit_node = head
            stack_num = []
            while num > 0:
                stack_num.append(num % 10)
                num //= 10
            cur_word_counter = 0
            while stack_num:
                digit = stack_num.pop()
                if digit not in cur_digit_node.childs:
                    break
                cur_digit_node = cur_digit_node.childs[digit]
                cur_word_counter += 1
            max_length = max(cur_word_counter, max_length)
        return max_length