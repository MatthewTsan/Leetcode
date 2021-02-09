from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find(i, j):
            print(i, j)
            if i == j:
                if target == nums[i]:
                    return i
                else:
                    return -1
            mid = (i + j) // 2
            if nums[i] <= nums[mid]:
                if target >= nums[i] and target <= nums[mid]:
                    return find(i, mid)
                else:
                    return find(mid + 1, j)
            else:
                if target > nums[mid] and target <= nums[j]:
                    return find(mid + 1, j)
                else:
                    return find(i, mid)

        return find(0, len(nums) - 1)