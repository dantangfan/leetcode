# coding:utf-8
# 直接用大数貌似不对

class Solution(object):
    int_to_char = {
        1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G',
        8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N',
        15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U',
        22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
    }

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ''
        res = ''
        while n:
            if n % 26:
                res = self.int_to_char[n % 26] + res
                n /= 26
            else:
                res = 'Z' + res
                n /= 26
                n -= 1
        return res

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        CHAR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = ''
        while n > 0:
            n -= 1
            res = CHAR[n % 26] + res
            n /= 26
        return res


print Solution().convertToTitle(111)