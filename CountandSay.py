# coding:utf-8

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ''
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        string = '11'
        for i in xrange(2, n):
            string = self.count(string)
        return string

    def count(self, string):
        start, end = 0, 1
        res = ''
        llen = len(string)
        for j in xrange(1, llen):
            if string[j] == string[j - 1]:
                end += 1
            else:
                res = res + str(end-start) + string[start]
                start = end
                end += 1
        res = res + str(end-start) + string[start]
        return res

print Solution().countAndSay(9)