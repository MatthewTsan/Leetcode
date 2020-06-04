class Solution:
    def removeDuplicates_1(self, nums) -> int:
        i = 0
        while i < len(nums)-1:
            # print(nums)
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1

        return len(nums)

    def removeDuplicates(self, nums) -> int:
        nums = list(set(nums))
        print(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
