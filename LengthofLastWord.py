# coding:utf-8
# 最后一个单词的长度

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s.strip():
            return 0
        return len(s.rsplit()[-1])

print Solution().lengthOfLastWord('   ')