# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer


class BadVersion(object):
    def __init__(self, n):
        self.badversion = n

    def isBadVersion(self, version):
        if version < self.badversion:
            return False
        else:
            return True


class Solution:
    def __init__(self, badBegin):
        self.badVersion = BadVersion(badBegin)

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            if self.badVersion.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left


BadBegin = 3
n = 10
sol = Solution(BadBegin)
print(sol.firstBadVersion(n))