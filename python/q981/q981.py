import bisect
from collections import defaultdict


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        l = self.map[key]
        if not l:
            return ""
        i = bisect.bisect(l, [timestamp, chr(127)])
        return l[i-1][1] if i else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)