"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
"""
from typing import List


class TrieNode:
    def __init__(self, val):
        self.val = val
        self.childs = dict()
        self.is_word = False


class Solution:
    def create_trie(self, words):
        head = TrieNode("")
        for word in words:
            cur = head
            for char in word:
                if char not in cur.childs:
                    cur.childs[char] = TrieNode(char)
                cur = cur.childs[char]
            cur.is_word = True
        return head

    def construct_words(self, board, row, col, seen_indices, trie, results, cur_word):
        char = board[row][col]
        # earliy pruning
        if char not in trie.childs:
            return
        # add char
        cur_word.append(char)
        trie = trie.childs[char]
        seen_indices.add((row, col))
        # check if found a word
        if trie.is_word:
            results.add("".join(cur_word))
        # keep the dfs
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for delta_row, delta_col in directions:
            new_row = delta_row + row
            new_col = delta_col + col
            if (new_row, new_col) not in seen_indices and new_row >= 0 and new_row < len(board) and new_col >= 0 and new_col < len(board[0]):
                self.construct_words(board, new_row, new_col, seen_indices, trie, results, cur_word)
        # remove the element when done and go one step up the dfs
        cur_word.pop()
        seen_indices.remove((row, col))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Solution - using trie for checking words including early pruning, dfs to raverse the board, set for seen indices while traversing the board.
        """
        if not board:
            if "" in words:
                return [""]
            else:
                return []

        trie = self.create_trie(words)
        results = set()

        for row in range(len(board)):
            for col in range(len(board[0])):
                self.construct_words(board, row, col, set(), trie, results, [])
        return list(results)