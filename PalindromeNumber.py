# coding:utf-8
# 判断数字是不是回文
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        c, d = 0, x
        while d:
            c, d = c * 10 + d % 10, d / 10
        return c == x

print Solution().isPalindrome(12321)