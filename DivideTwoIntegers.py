# coding:utf-8
# 不用 * / % 求除法
# 最简单的就是每次用减法,但是会超时
# 然后就每次减去除数的倍数,就不会超时了
# 类似的还有求平方根
# 求 a 的平方根, 先随便找一个数 x ,然后每次 x = (x + a/x) 就可以快速找到平方根
class Solution(object):
    MAX_INT = (1 << 31) - 1
    MIN_INT = -(1 << 31)

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0 or dividend > self.MAX_INT or divisor > self.MAX_INT or dividend < self.MIN_INT or divisor < self.MIN_INT:
            return self.MAX_INT
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            flag = 1
        else:
            flag = -1

        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while True:
            if dividend < divisor:
                break
            res += 1
            dividend -= divisor
        if flag:
            return res
        return -res

class Solution(object):
    MAX_INT = (1 << 31) - 1
    MIN_INT = -(1 << 31)

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0 or dividend > self.MAX_INT or divisor > self.MAX_INT or dividend < self.MIN_INT or divisor < self.MIN_INT:
            return self.MAX_INT
        flag = (dividend ^ divisor) >> 31
        a, b = abs(dividend), abs(divisor)
        res = 0
        while a >= b:
            c = b
            i = 0
            while a >= c:
                a -= c
                res += (1 << i)
                c <<= 1
                i += 1
        if flag < 0:
            res = -res
        if res > self.MAX_INT or res < self.MIN_INT:
            return self.MAX_INT
        return res

print Solution().divide(1 ,1)