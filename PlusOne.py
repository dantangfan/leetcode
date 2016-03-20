# coding:utf-8
# 对他进行加1操作
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        llen = len(digits) - 1
        for i in xrange(llen, -1, -1):
            digits[i] = (digits[i] + 1) % 10
            if digits[i]:
                break
        else:
            digits.insert(0, 1)
        return digits


print Solution().plusOne([1,0])
