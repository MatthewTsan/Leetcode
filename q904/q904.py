from typing import List

"""
keyPoint:
    sliding window. facing problems with multiple same numbers: consider sum it up.
"""



class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if len(tree) == 0:
            return 0

        treeList = []
        totalNumber = 1
        for i in range(len(tree) - 1):
            if tree[i] == tree[i + 1]:
                totalNumber += 1
            else:
                treeList.append((tree[i], totalNumber))
                totalNumber = 1
        treeList.append((tree[-1], totalNumber))
        print(treeList)

        if(len(treeList) == 1):
            return treeList[0][1]

        i = 2
        inBusket = [treeList[0][0], treeList[1][0]]
        temWeight = treeList[0][1] + treeList[1][1]
        maxWeight = temWeight
        while (i < len(treeList)):
            print(i)
            print("inBusket:", inBusket)
            print("temWeight:", temWeight)
            print("max:", maxWeight)
            if treeList[i][0] in inBusket:
                temWeight += treeList[i][1]
            else:
                maxWeight = max(temWeight, maxWeight)
                inBusket = [treeList[i - 1][0], treeList[i][0]]
                temWeight = treeList[i - 1][1] + treeList[i][1]
            i += 1
        maxWeight = max(temWeight, maxWeight)

        return maxWeight


if __name__ == '__main__':
    sol = Solution()
    list = [1, 1,1,1,1,1]
    res = sol.totalFruit(list)
    print(res)
