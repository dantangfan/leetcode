# coding:utf-8
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        print n
        if n == 0:
            return False
        if n % 3:
            return False
        return self.isPowerOfThree(n / 3)

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n:
            return False
        while n:
            if n == 1:
                return True
            if n % 3:
                return False
            n /= 3
        return False

class Solution(object):
    # 1162261467 是 int 下面最大的 n 的次方
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n > 0) and (1162261467 % n == 0)

print Solution().isPowerOfThree(27)