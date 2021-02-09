from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        out = defaultdict(list)
        inNum = defaultdict(int)
        for w in words:
            for i in range(len(w)):
                out[w[i]] = []
                inNum[w[i]] = 0

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j == len(words[i + 1]):
                    return ""
                if words[i][j] != words[i + 1][j]:
                    out[words[i][j]].append(words[i + 1][j])
                    inNum[words[i + 1][j]] = inNum[words[i + 1][j]] + 1
                    break

        deq = deque()
        ans = []
        for c in inNum:
            if inNum[c] == 0:
                deq.append(c)

        while deq:
            c = deq.popleft()
            ans.append(c)
            for outC in out[c]:
                inNum[outC] -= 1
                if inNum[outC] == 0:
                    deq.append(outC)
        if len(ans) == len(inNum):
            return "".join(ans)
        else:
            return ""
