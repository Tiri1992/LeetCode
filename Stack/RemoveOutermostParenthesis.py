"""
Leetcode Question: Remove outer most parenthesis 

url: https://leetcode.com/problems/remove-outermost-parentheses/
"""

S = "(()())(())(()(()))"
mapper = {'(': ')', ')': '('}


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        o = 0
        r = ""
        for i in range(len(S)):
            if S[i] == '(':
                o += 1
            if o > 1:
                r += S[i]
            if S[i] == ')':
                o -= 1
        return r


if __name__ == '__main__':
    s = Solution()
    s.removeOuterParentheses(S)
