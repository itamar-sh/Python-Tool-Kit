from typing import List


class TrieNode:
    def __init__(self, name):
        self.name = name
        self.childs = dict()
        self.is_folder = False


class Solution:
    """
    Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.

    If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".

    The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

    For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.

    """
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        # Init Trie of folders
        head = TrieNode("")
        for folder in folders:
            cur_dir = head
            for directory in folder.split("/"):  # first case is always empty string
                if directory not in cur_dir.childs:
                    cur_dir.childs[directory] = TrieNode(directory)
                cur_dir = cur_dir.childs[directory]
                # In case of parent directory ditacted - early break
                if cur_dir.is_folder:
                    break
            cur_dir.is_folder = True
        # Check for only parent folder in Trie
        res = []
        for folder in folders:
            cur_dir = head
            for directory in folder.split("/")[:-1]:  # last case is always good choise
                cur_dir = cur_dir.childs[directory]
                # In case of parent directory ditacted - early break
                if cur_dir.is_folder:
                    break
            else:   # All the folder is contained inside the Trie - good case
                res.append(folder)
        return res