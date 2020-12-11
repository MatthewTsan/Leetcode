from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        min = 0
        current = 0
        index = -1
        for i in range(len(gas)):
            current += gas[i] - cost[i]
            if min > current:
                min = current
                index = i

        return -1 if current < 0 else index + 1