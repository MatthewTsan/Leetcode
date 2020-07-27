from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        list = ["" for i in range(len(indices))]
        for c, i in zip(s, indices):
            list[i] = c
        return "".join(list)

    def restoreString_2(self, s: str, indices: List[int]) -> str:
        dict = {}
        res = ""
        for c, i in zip(s, indices):
            dict[i] = c
        indices.sort()
        for i in indices:
            res += dict[i]

        return res

sol = Solution()
list = [3,1,4,2,0]
res = sol.restoreString_2("aiohn", list)
print(res)