# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from heapq import heappush, heappop
from typing import Optional

class Solution:
    """
    You are given the root of a binary tree and a positive integer k.

    The level sum in the tree is the sum of the values of the nodes that are on the same level.

    Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

    Note that two nodes are on the same level if they have the same distance from the root.
    """
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # min_heap will hold the k largest numbers each time
        min_heap = []
        # using bfs to calculate all the level sum
        cur_level = [root]
        while cur_level:
            next_level = []
            level_sum = 0
            for node in cur_level:
                level_sum += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur_level = next_level
            # update min_heap
            if len(min_heap) < k:
                heappush(min_heap, level_sum)
            elif level_sum > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, level_sum)
        return min_heap[0] if len(min_heap) == k else -1