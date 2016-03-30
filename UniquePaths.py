# coding:utf-8
# 不管怎么走,需要走 m-1+n-1 次,只需要从里面挑出其中 m-1 次向下就行了就是 C(m+n-2)(m-1)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        x = m+n-2
        y = m-1
        if x-y > y:
            y = n - 1
        a, b = 1, 1
        tmp = y
        while tmp:
            a *= x
            x -= 1
            tmp -= 1
        while y:
            b *= y
            y -= 1
        return a/b

print Solution().uniquePaths(3,2)