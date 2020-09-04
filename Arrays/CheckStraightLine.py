"""
Leetcode Question: Check if it is a straight line

url: https://leetcode.com/problems/check-if-it-is-a-straight-line/
"""
from typing import List, Tuple

coordinates = [[0, 0], [0, 1], [0, -1]]


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Straight lines -> y = mx + c
        # Pick two points
        p1 = coordinates[0]
        p2 = coordinates[1]

        m, c = self.get_gradient_intercept(p1, p2)
        if m != 0:
            def f(x): return m * x + c
            # if its a straight line:
            validity = [row[1] == f(row[0]) for row in coordinates]
            return all(validity)
        else:
            # either horizontal or vertical
            if self.all_array_equal(coordinates, 0):
                # vertical
                return True
            elif self.all_array_equal(coordinates, 1):
                return True
            else:
                return False

    def get_gradient_intercept(self, p1: List[int], p2: List[int]) -> Tuple[int]:
        if (p2[0] - p1[0]) != 0:
            m = (p2[1] - p1[1]) / (p2[0] - p1[0])
        else:
            m = 0
        c = p2[1] - p2[0] * m
        return m, c

    def all_array_equal(self, arr: List[int], index: int) -> bool:
        val = arr[0][index]
        return all([row[index] == val for row in arr])


if __name__ == '__main__':
    s = Solution()
    print(s.checkStraightLine(coordinates))
