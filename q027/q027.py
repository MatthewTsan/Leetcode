from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while(val in nums):
            nums.remove(val)
        return len(nums)

if __name__ == '__main__':
    solution = Solution()
    listNums = [3,2,2,3]
    solution.removeElement(listNums, 2)
    print(listNums)