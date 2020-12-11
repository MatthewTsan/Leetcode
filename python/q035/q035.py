from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)


if __name__ == '__main__':
    solution = Solution()
    listNums = [1,3,5,6]
    print(solution.searchInsert(listNums, 0))