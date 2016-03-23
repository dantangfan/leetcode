class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        res = {}
        for i, v in enumerate(nums):
            if res.get(v, None) is not None and i - res.get(v) <= k:
                return True
            else:
                res[v] = i
        return False

print Solution().containsNearbyDuplicate([-1, -1], 1)
