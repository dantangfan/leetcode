# coding:utf-8
# 跟某个题一样,需要双向考虑
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern = list(pattern)
        string = str.split()
        res = {}
        if len(pattern) != len(string):
            return False
        for i, v in enumerate(pattern):
            if res.get(v) and res[v] != string[i]:
                return False
            else:
                res[v] = string[i]
        res = {}
        for i, v in enumerate(string):
            if res.get(v) and res[v] != pattern[i]:
                return False
            else:
                res[v] = pattern[i]
        return True