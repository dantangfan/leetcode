class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        llen = len(nums)
        res = {}
        for i in xrange(llen):
            if res.get(nums[i]):
                return True
            res[nums[i]] = 1
        return False

print Solution().containsDuplicate()