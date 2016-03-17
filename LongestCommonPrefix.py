# coding:utf-8
# 求字符串的最长公共前缀
# 1.暴力求解，一次匹配每个字符串的某位
# 2.每次对比两个字符串，直到有不同，然后用其中一个字符串于下面一条想比较，直到上次不同的位置，这样肯定比1还慢
# 3.每次弹出字符串第i个位置到set中，看set长度是否为1，不为1说明有不同了
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs_len = len(strs)
        if strs_len == 0:
            return ''
        if strs_len == 1:
            return strs[0]
        min_len = min([len(s) for s in strs])
        i = 0
        while i < min_len:
            prefix_i = strs[0][i]
            for j in range(1, strs_len):
                if strs[j][i] != prefix_i:
                    return strs[0][:i]
            i += 1
        return strs[0][:i]


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs_len = len(strs)
        if strs_len == 0:
            return ''
        if strs_len == 1:
            return strs[0]
        j = 0
        while 1:
            s = set()
            try:
                for i in xrange(strs_len):
                    s.add(strs[i][j])
                if len(s) != 1:
                    return strs[0][:j]
                j += 1
            except:
                return strs[0][:j]


print Solution().longestCommonPrefix([ 'abc', 'abaaa'])
