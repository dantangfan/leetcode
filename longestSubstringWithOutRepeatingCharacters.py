# coding:utf-8
# 求最长无重复字符串
# 最简单的办法就是直接两次循环，直接暴力解出来
# 这里我记录了一个字母的最后出现位置，和这个字母重复时候的最大长度
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = {}
        maxlen, start = 0, 0
        for i, v in enumerate(s):
            if pos.get(v, None) is None:
                l = i - start + 1
                pos[v] = [i, l]
                #print 'haha', start, pos, l, i ,maxlen, v
            else:
                d = min(i - pos[v][0], i - start + 1)
                #print start, pos[v], d, i, maxlen, v
                if d > pos[v][1]:
                    pos[v][1] = d
                start = max(pos[v][0] + 1, start)
                pos[v][0] = i
            maxlen = maxlen if maxlen > pos[v][1] else pos[v][1]
        return maxlen



s = Solution()
print s.lengthOfLongestSubstring('aasdddddddabssssadvckkk')
