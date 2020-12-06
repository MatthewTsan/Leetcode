# 1 sort with some condition
# q937

sorted(iterable, cmp=None, key=None, reverse=False)

```python
from typing import List
class _1:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )
            return sorted(logs, key=get_key)
```

# 2 queue
use collections.deque
```python
from collections import dequeue
q = dequeue() # q is a iterable, like List[]

# put:
q.append(value)

# pop:
q.popleft()
```

# 3 DSU 并查集
```python
class DSU:
    def __init__(self, capacity):
        self.p = range(capacity)
        
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
```