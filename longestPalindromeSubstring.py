# coding:utf-8
# 求最大回文
# 1.可以两层循环判断依次判断开始和结束，第三层循环判断回文 复杂度n3
# 2.利用回文的对称性，分别以第1个字符到第n-2个字符为中心，分两次判断奇数个字符时候的回文和偶数个字符的回文复杂度n2

class Solution(object):
    """
    直接用方法 2
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        final_start, final_end = 0, 0
        length = len(s)
        for center in range(0, length-1):
            # 奇数情况
            tmp_start, tmp_stop = center, center
            while tmp_start >= 0 and tmp_stop < length and s[tmp_start] == s[tmp_stop]:
                tmp_start -= 1
                tmp_stop += 1
            tmp_start, tmp_stop = tmp_start + 1, tmp_stop - 1
            if tmp_stop - tmp_start > final_end - final_start:
                final_start, final_end = tmp_start, tmp_stop

            # 偶数情况
            tmp_start, tmp_stop = center, center + 1
            while tmp_start >= 0 and tmp_stop < length and s[tmp_start] == s[tmp_stop]:
                tmp_start -= 1
                tmp_stop += 1
            tmp_start, tmp_stop = tmp_start + 1, tmp_stop - 1
            if tmp_stop - tmp_start > final_end - final_start:
                final_start, final_end = tmp_start, tmp_stop
        return s[final_start: final_end+1]

class Solution1(object):
    """
    为了不用判断奇偶数，可以直接在每两个字母之间加入间隔符 「@」
    这样，就不可能有连续两个字符一样
    然而，这样增大了 str 的长度，可能造成超时
    """
    def longestPalindrome(self, s):
        s1 = '@'.join([_ for _ in s])
        fstart, fend = 0, 0
        length = len(s1)
        for c in range(length):
            tstart, tend = c, c
            while tstart >= 0 and tend < length and s1[tstart] == s1[tend]:
                tstart -= 1
                tend += 1
            tstart += 1
            tend -= 1
            if tend - tstart > fend - fstart:
                fstart, fend = tstart, tend
        res = s1[fstart:fend+1]
        res = filter(lambda _: _ != '@', res)
        return res


s = Solution()
print s.longestPalindrome("abbaabba")


