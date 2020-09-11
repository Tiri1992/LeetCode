"""
Leetcode Question: Given two strings A and B return True iff two letters 
can be swapped in A to equal B.

url: https://leetcode.com/problems/buddy-strings/
"""

from collections import Counter

A = "ab"
B = "ba"


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        A_count = Counter(A)
        B_count = Counter(B)
        if A_count != B_count:
            return False
        if (len(A) == 0) or (len(B) == 0):
            return False
        if A == B:
            if A_count.most_common(1)[0][1] > 1:
                # means we can just swap most two of the same letters
                return True
            else:
                return False
        if A_count == B_count:
            # No more than two misplaced
            not_equal_elements = [i != j for i, j in zip(A, B)]
            if sum(not_equal_elements) > 2:
                return False
            else:
                return True


if __name__ == '__main__':
    s = Solution()
    print(s.buddyStrings(A, B))
