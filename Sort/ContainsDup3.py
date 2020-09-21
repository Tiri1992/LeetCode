"""
Leetcode Question: Find out whether there are two distinct indices i and j in the array
such that the absolute difference between nums[i] and nums[j]
is at most t and the absolute difference between i and j is at most k.

url: https://leetcode.com/problems/contains-duplicate-iii/
"""
from typing import List
from collections import deque
# Example: True
nums = [1, 5, 9, 1, 5, 9]
k = 2
t = 3


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False
        # contains duplicates your done:
        queue = deque(maxlen=k)
        last_pos = {}
        for idx, n in nums:
            if n in last_pos:
                # exists already:
                pos = last_pos[n]
                if abs(pos - idx) <= k:
                    return True
            if n not in last_pos:
                last_pos[n] = idx
            if idx % k == 0:
                # Reset
                unique_nums = set()
                last_pos = {}


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyAlmostDuplicate(nums, k, t))
