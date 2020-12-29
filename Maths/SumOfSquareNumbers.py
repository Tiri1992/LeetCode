"""
Leetcode Question: Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

url: https://leetcode.com/problems/sum-of-square-numbers/
"""
import math

c = 1


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Reverse a^2 = c - b^2
        r = int(math.sqrt(c))
        if self.is_square(c):
            # If C a square number, one can be 0
            return True
        for b in range(1, r + 1):
            a_2 = c - pow(b, 2)
            if a_2 == 0:
                return False
            if self.is_square(a_2):
                return True
        return False

    def is_square(self, val: int) -> bool:
        return math.isqrt(val) == math.sqrt(val)


if __name__ == '__main__':
    s = Solution()
    print(s.judgeSquareSum(c))
