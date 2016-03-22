class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = list(bin(n)[2:])
        b.reverse()
        diff = 32 - len(b)
        for i in xrange(diff):
            b.append('0')
        return int(''.join(b), base=2)


class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in xrange(31, -1, -1):
            tmp = n & 1
            n >>= 1
            res |= (tmp << (i))
        return res

print Solution().reverseBits(43261596)