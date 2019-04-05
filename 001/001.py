class Solution:
    def twoSum(self, nums, target):
        # print(nums[:len(nums) -1 ])
        # print(nums[0+1:])
        for num1, item1 in enumerate(nums[:len(nums) -1]):
            for num2, item2 in enumerate(nums[num1+1:]):
                # print(item1, item2)
                if item1 + item2 == target:
                    return [num1, num1+num2+1]
        return []


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 26))