"""
Leetcode Question: Unique email addresses

url: https://leetcode.com/problems/unique-email-addresses/
"""

import re
from typing import List

data = ["test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        pattern_1 = r'\+[A-Za-z\.]+'
        pattern_2 = r'\.+(?=[A-Za-z\.]+@)'
        for d in emails:
            result1 = re.sub(pattern_1, '', d)
            final = re.sub(pattern_2, '', result1)
            unique.add(final)
        return len(unique)


if __name__ == '__main__':
    s = Solution()
    print(s.numUniqueEmails(emails=data))
