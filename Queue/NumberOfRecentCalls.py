"""
LeetCode: Queues

url: https://leetcode.com/problems/number-of-recent-calls/
"""


class RecentCounter:

    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def ping(self, t: int) -> int:
        self.queue.append(t)
        lower = t - 3000
        while (self.queue[0] < lower):
            del self.queue[0]
        return len(self)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
