# coding:utf-8
# 看一个数是否是2的倍数,
# 看一共有多少个 1
# n & (n-1) 一定为 0

class Solution(object):
    # 超时
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        while n:
            count += (n & 1)
            n >>= 1
        return count <= 1


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n > 0 and not n & (n - 1))