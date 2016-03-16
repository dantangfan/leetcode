class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        overflow = 1 << 31
        lsx = list(str(x))
        if lsx[0] == '-':
            sx = lsx[1:]
            sx.reverse()
            sx = '-' + ''.join(sx)
        else:
            lsx.reverse()
            sx = ''.join(lsx)
        sx = int(sx)
        return sx if -overflow <= sx <= overflow-1 else 0

class Solution(object):
    def reverse(self, x):
        b = x if x > 0 else -x
        a = 0
        overflow = 1 << 31
        while b:
            a = a * 10 + b % 10
            b /= 10
        a = a if x > 0 else -a
        return a if -overflow<=a<overflow-1 else 0

print Solution().reverse(-12324388843)