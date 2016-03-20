# coding:utf-8
# 台阶问题

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in (1, 2):
            return n
        a, b = 2, 1
        for i in xrange(2, n):
            a, b = a+b, a
        return a

print Solution().climbStairs(5)