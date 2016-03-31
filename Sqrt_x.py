# coding:utf-8
# 牛顿迭代法求平方根


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = x / 2.0
        while abs(res*res-x) > 0.1:
            res = (res + x/res) / 2.0
        return int(res)

print Solution().mySqrt(1)