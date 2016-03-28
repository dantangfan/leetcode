# coding:utf-8
# 求浮点数的次方,要注意 n 是否为负数
# 最简单的解法就是直接一次乘以一个 x
# 还有就是二分法, 下一次的结果是上一次的平方
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1.0 / self.pow(x, -n)
        return self.pow(x, n)

    def pow(self, x, n):
        if n == 0:
            return 1
        v = self.pow(x, n / 2)
        if n % 2 == 0:
            return v * v
        else:
            return v * v * x

s = Solution()
print s.pow(2, 10)