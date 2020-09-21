"""
Leetcode Question: Given an integer n. Each number from 1 to n is grouped according to the sum of its digits. 

Return how many groups have the largest size.

url: https://leetcode.com/problems/count-largest-group/
"""


import math

# Example:
n = 13


class Solution:
    def countLargestGroup(self, n: int) -> int:
        counter = {}
        p = math.floor(math.log10(n))
        for i in range(1, n + 1):
            # string conversion:
            i_str = str(i)
            total = 0
            for r in i_str:
                total += eval(r)
            if total in counter:
                counter[total] += 1
            else:
                counter[total] = 1
        max_val = max(counter.values())
        groups = 0
        for k, v in counter.items():
            if v == max_val:
                groups += 1
        return groups


if __name__ == '__main__':
    s = Solution()
    print(s.countLargestGroup(n))
