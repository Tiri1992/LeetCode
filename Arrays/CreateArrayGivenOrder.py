"""
Leetcode Question: Create an array given order

url: https://leetcode.com/problems/create-target-array-in-the-given-order/
"""

from typing import List

nums = [1, 2, 3, 4, 0]
index = [0, 1, 2, 3, 0]


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for n, idx in zip(nums, index):
            target.insert(idx, n)
        return target


if __name__ == '__main__':
    s = Solution()
    print(s.createTargetArray(nums, index))
