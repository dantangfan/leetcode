# coding:utf-8
# 本来想用动态规划,但是数字中间会出现0,状态转移方程不好弄
# 比如, 110, 11 有两种 110却只有一种
# 所以还是递归回溯吧, 可悲的是,递归回溯超时了.
# 所以最后还是动态规划吧

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or not int(s):
            return 0
        llen = len(s)
        res = [0]
        self.helper(s, 0, llen, res)
        return res[0]

    def helper(self, s, index, llen, res):
        if index == llen:
            res[0] += 1
            return
        if 0 < int(s[index]) <= 9:
            self.helper(s, index+1, llen, res)
        if index + 1 < llen and 10 <= int(s[index: index+2]) <= 26:
            self.helper(s, index+2, llen, res)

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        llen = len(s)
        if llen == 1:
            return 1
        res = [0] * llen
        res[0] = 1
        if int(s[1]) == 0:
            if int(s[0]) <= 2:
                res[1] = 1
            else:
                res[1] = 0
        elif 0 < int(s[0:2]) <= 26:
            res[1] = 2
        else:
            res[1] = 1
        for i in xrange(2, llen):
            if 1 <= int(s[i]) <= 9:
                res[i] += res[i-1]
            if int(s[i-1]) != 0 and 10 <= int(s[i-1:i+1]) <= 26:
                res[i] += res[i-2]
        return res[llen-1]

print Solution().numDecodings('301')