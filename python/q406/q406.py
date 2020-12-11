from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        people.sort(key=lambda x: (-x[0], x[1]))

        for x in people:
            ans.insert(x[1], x)
        return ans


sol = Solution()
list = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(sol.reconstructQueue(list))
