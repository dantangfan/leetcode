# coding:utf-8
# 根据题意
# 当 n=4 时, 先走的无论是 1,2,3 都会输
# 当 n=[5, 6, 7] 时, 先走的,都可以造成剩下的是 4 个,于是后走的都会输
# 由上可知,只要保证先走的人走后, 剩下的是4的倍数,就能赢.于是,只要数量本身不是4的倍数就行
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 > 0