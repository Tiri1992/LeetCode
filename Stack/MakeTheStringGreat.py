"""
Leetcode Question: Make the String Great

url: https://leetcode.com/problems/make-the-string-great/
"""
example_s = "leEeetcode"


class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) == 0:
            # Automatically a good string
            return s
        # implement a stack
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            elif stack[-1] == s[i]:
                # Allowed as they are not opposite in caps
                stack.append(s[i])
            elif stack[-1].upper() == s[i]:
                # remove the element in stack
                stack.pop()
            elif stack[-1] == s[i].upper():
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)


if __name__ == '__main__':
    s = Solution()
    print(s.makeGood(example_s))
