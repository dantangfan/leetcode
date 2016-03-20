# coding:utf-8
# 二进制加法
# 常规解法，大数加法
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        if not b:
            return a
        return bin(int(a, base=2) + int(b, base=2))[2:]


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        if not b:
            return a
        lena = len(a)
        lenb = len(b)
        llen = lena
        if lena != lenb:
            if lena > len(b):
                b = '0'*(lena-lenb) + b
                llen = lena
            else:
                a = '0' * (lenb - lena) + a
                llen = lenb
        carry = 0
        res = []
        for i in xrange(llen-1, -1, -1):
            r = (int(a[i]) + int(b[i]) + carry) % 2
            carry = (int(a[i]) + int(b[i]) + carry) / 2
            res.append(r)
        if carry:
            res.append(1)
        res.reverse()
        return ''.join([str(_) for _ in res])

print Solution().addBinary('11','1')
