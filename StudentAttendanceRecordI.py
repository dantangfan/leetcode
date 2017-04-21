class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a, l = 0, 0
        for i in s:
            if i == 'A':
                l = 0
                a += 1
                if a > 1:
                    return False
            elif i == 'L':
                l += 1
                if l > 2:
                    return False
            else:
                l = 0
        return True


s = Solution()
print s.checkRecord("PPALLP")
print s.checkRecord("PPALLL")
