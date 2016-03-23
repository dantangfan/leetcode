# coding:utf-8
# 判断s是否能经过字母替换变成t,字母的位置要一一对应
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slen, tlen = len(s), len(t)
        if slen != tlen:
            return False
        res = {}
        for i in xrange(slen):
            if not res.get(s[i]):
                res[s[i]] = t[i]
            elif res[s[i]] != t[i]:
                return False
        res = {}
        for i in xrange(slen):
            if not res.get(t[i]):
                res[t[i]] = s[i]
            elif res[t[i]] != s[i]:
                return False
        return True


print Solution().isIsomorphic('bb', 'aa')
