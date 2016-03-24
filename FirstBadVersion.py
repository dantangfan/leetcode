# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        if isBadVersion(1):
            return 1
        while low <= high:
            cur = low + (high - low) / 2
            cur_bad = isBadVersion(cur)
            if not cur_bad:
                low = cur + 1
                continue
            if cur_bad and not isBadVersion(cur - 1):
                return cur
            else:
                high = cur - 1
                continue
