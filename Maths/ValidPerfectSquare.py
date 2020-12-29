"""
Leetcode Question: Check if num is a valid perfect square

NOTE: You're not allowed to use any built-in sqrt function.

url: https://leetcode.com/problems/valid-perfect-square/
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        while True:
            if (i ** 2) == num:
                return True
            if (i ** 2) > num:
                return False
            i += 1


s = Solution()
print(s.isPerfectSquare(16))
