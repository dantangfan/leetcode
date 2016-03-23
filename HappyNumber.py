# coding:utf-8
# 按照题意,一直计算到值为1或者出现循环即可
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = {}
        while n:
            tmp = 0
            while n:
                pos = n % 10
                tmp += pos*pos
                n /= 10
            if tmp == 1:
                return True
            if nums.get(tmp):
                return False
            nums[tmp] = 1
            n = tmp
        return False

print Solution().isHappy(0)
