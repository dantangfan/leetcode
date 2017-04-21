from collections import Counter
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return sum(v>1 for v in Counter(nums).values())
        elif k > 0:
            return len(set(nums)&set(n+k for n in nums))
        return 0


