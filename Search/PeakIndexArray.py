"""
Leetcode Question: 

Conditions:
- arr[0] < arr[1] < ... arr[i-1] < arr[i]
- arr[i] > arr[i+1] > ... > arr[arr.length - 1]

url: https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""
from typing import List

arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max_idx = arr.index(max(arr))
        return max_idx


if __name__ == '__main__':
    s = Solution()
    print(s.peakIndexInMountainArray(arr))
