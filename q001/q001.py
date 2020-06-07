from functools import reduce

class HashMap:
    LargeNumber = 509

    def __init__(self, target, length):
        self.__target = abs(target)
        self.__list = [[] for i in range(min(length, self.LargeNumber))]

    def __hashCode(self, value):
        return (abs(self.__target - abs(value))) % self.LargeNumber

    def insert(self, key, value):
        hashResult = self.__hashCode(key)
        self.__list[hashResult].append((key, value))

    def getHash(self, key):
        hashResult= self.__hashCode(key)
        if self.__list[hashResult]:
            return self.__list[hashResult]
        else:
            raise KeyError



class Solution:
    def twoSum_1(self, nums, target):
        # print(nums[:len(nums) -1 ])
        # print(nums[0+1:])
        for num1, item1 in enumerate(nums[:len(nums) -1]):
            for num2, item2 in enumerate(nums[num1+1:]):
                # print(item1, item2)
                if item1 + item2 == target:
                    return [num1, num1+num2+1]
        return []

    def twoSum(self, nums, target):
        hashMap = HashMap(target, 2 * reduce(lambda x, y: abs(x) if abs(x) > abs(y) else abs(y), nums, abs(nums[0])))
        for i, item in enumerate(nums):
            hashMap.insert(item, i)

        for i, item in enumerate(nums):
            complement = target - item
            try:
                hashResult = hashMap.getHash(complement)
            except:
                hashResult = []
            if hashResult:
                for key, value in hashMap.getHash(complement):
                    if value != i and item + nums[value] == target:
                        return [i, value]


if __name__ == '__main__':
    solution = Solution()
    list = [2, 7, 11, 15]
    # list = [-1, -2, 2, -3, -4, -5]
    # list = [5000000000, 1, 2, 3, 5000000000]

    print(solution.twoSum(list, 18))
