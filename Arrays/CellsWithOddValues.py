"""
Leetcode Question: Return number of cells with odd values

url: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
"""
from typing import List
from collections import Counter

n, m = 2, 3
indicies = [[0, 1], [1, 1]]


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row_count = Counter([row[0] for row in indices])
        col_count = Counter([row[1] for row in indices])
        count = 0
        for i in range(n):
            for j in range(m):
                num = row_count.get(i, 0) + col_count.get(j, 0)
                if num % 2 != 0:
                    count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.oddCells(n, m, indicies))
