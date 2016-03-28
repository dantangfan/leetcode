# coding:utf-8
# 求数组连续项的最大和
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        cur = 0
        for i, v in enumerate(nums):
            if cur <= 0:
                cur = 0
            cur += v
            max_sum = max(cur, max_sum)
        return max_sum

print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])