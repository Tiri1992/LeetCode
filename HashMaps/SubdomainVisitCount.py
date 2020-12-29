""" 
Leetcode Question: Subdomain visit count

url: https://leetcode.com/problems/subdomain-visit-count/
"""
from typing import List
from collections import defaultdict

cpdomains = ["900 google.mail.com", "50 yahoo.com",
             "1 intel.mail.com", "5 wiki.org"]


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        top = defaultdict(int)
        middle = defaultdict(int)
        bottom = defaultdict(int)
        # Full domain (i.e. with 2 dots will not contain any more)
        for data in cpdomains:
            # Split
            count, domain = data.split(" ")
            # Change data type str -> int
            count = int(count)
            count_dots = domain.count(".")
            if count_dots == 2:
                # top, middle, bottom:
                b, m, t = domain.split(".")
                top[t] += count
                middle['.'.join([m, t])] += count
                bottom['.'.join([b, m, t])] += count
            elif count_dots == 1:
                # middle, top:
                m, t = domain.split(".")
                top[t] += count
                middle['.'.join([m, t])] += count
        results = []
        for d, c in top.items():
            results.append(" ".join([str(c), d]))
        for d, c in middle.items():
            results.append(" ".join([str(c), d]))
        for d, c in bottom.items():
            results.append(" ".join([str(c), d]))
        return results


if __name__ == "__main__":
    s = Solution()
    print(s.subdomainVisits(cpdomains))
