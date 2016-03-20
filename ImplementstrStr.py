# coding:utf-8
# 我天，简直不敢相信
# 1. 最简单快捷的办法当然是直接使用 python 字符串的 find 函数啦
# 2. KMP 算法，难理解、难编码、记不住，十分不推荐
# http://blog.csdn.net/WINCOL/article/details/4795369

class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)
