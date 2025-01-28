"""
120. Triangle
Solved
Medium
Topics
Companies

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.



Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:

Input: triangle = [[-10]]
Output: -10



Constraints:

    1 <= triangle.length <= 200
    triangle[0].length == 1
    triangle[i].length == triangle[i - 1].length + 1
    -104 <= triangle[i][j] <= 104


Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        older_dp = [triangle[0][0]]
        new_dp = []
        for row_index in range(1, len(triangle)):
            new_dp.append(older_dp[0] + triangle[row_index][0])
            for val_index in range(1, len(triangle[row_index])-1):
                new_dp.append(min(older_dp[val_index-1], older_dp[val_index]) + triangle[row_index][val_index])
            new_dp.append(older_dp[-1]+triangle[row_index][-1])

            older_dp = new_dp
            new_dp = []
        return min(older_dp)
