"""
Leetcode Question: Given the array nums, obtain a subsequence of the array whose sum of elements 
is strictly greater than the sum of the non included elements in such subsequence.

url: https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/
"""
from typing import List

# Example:
nums = [4, 3, 10, 9, 8]


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        # Sort order: Desc
        nums.sort(reverse=True)
        # Subset A starts as sum of all elements
        subset_A = sum(nums)
        # Subset B is our target
        subset_B = 0
        # Record the list of elements
        B = []
        for n in nums:
            # remove from subset_A
            subset_A -= n
            # add to subset_B
            subset_B += n
            # Append to B
            B.append(n)
            # Stop when subset_B first becomes > subset_A
            if subset_B > subset_A:
                break
        return B


if __name__ == '__main__':
    s = Solution()
    # Ans: [10, 9]
    print(s.minSubsequence(nums))
