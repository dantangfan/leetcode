# coding:utf-8
# 输出所有的子集,子集内部需要从小到大排序
# 直接递归回溯就行
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        llen = len(nums)
        res = [[]]
        if not llen:
            return res
        nums.sort()
        self.helper(nums, llen, 0, [], res)
        return res

    def helper(self, nums, llen, index, cur, res):
        for i in xrange(index, llen):
            cur.append(nums[i])
            res.append([_ for _ in cur])
            self.helper(nums, llen, i+1, cur, res)
            cur.pop()

a = [4, 1,0]
print Solution().subsets(a)
