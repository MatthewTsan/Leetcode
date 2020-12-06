import collections
from typing import List


class DSU:
    def __init__(self):
        self.p = list(range(10001))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()
        emlToId = {}
        emlToNm = {}
        id = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                emlToNm[email] = name
                if email not in emlToId:
                    emlToId[email] = id
                    id += 1
                dsu.union(emlToId[acc[1]], emlToId[email])

        ans = collections.defaultdict(list)
        for email in emlToNm:
            ans[dsu.find(emlToId[email])].append(email)

        return [[emlToNm[v[0]]] + sorted(v) for v in ans.values()]

