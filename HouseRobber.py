# coding:utf-8
# 偷东西,不能偷连续两家,求最多能偷多少
# 动态规划
# 只有一家的时候 res = home[0]
# 有两家的时候 res = max(home[0], home[1])
# 有 i 家的时候 res[i] = max( res[i-1], res[i-2] + home[i] )
# 这里可能有个疑问, res[i-1] 有没有可能不包括 home[i-].
# 无所谓,在这种情况下res[i-1]等同于res[i-2]，因此前者不会更小
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        llen = len(nums)
        if not llen:
            return 0
        if llen == 1:
            return nums[0]
        if llen == 2:
            return max(nums)
        res = [0] * llen
        res[0] = nums[0]
        res[1] = max(nums[:2])
        for i in xrange(2, llen):
            res[i] = max(res[i-1], res[i-2] + nums[i])
        return res[-1]

print Solution().rob([2,7,4])
