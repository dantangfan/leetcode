# coding:utf-8
# 格雷码,忘得差不多了
# 滴 n+1 个格雷码是第 n 个格雷码加上第 n 个反向并在头部加'1'
# n=1 的格雷码
# 0
# 1
# n=2 的格雷码
# 00
# 01
# 11
# 10
# n=3 的格雷码
# 000
# 001
# 011
# 010
# 110
# 111
# 101
# 100


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        llen = 1
        for i in xrange(n):
            add_head = 1 << i
            for j in xrange(llen-1, -1, -1):
                res.append(add_head+res[j])
            llen *= 2
        return res

print Solution().grayCode(0)
