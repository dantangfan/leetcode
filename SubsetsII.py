# coding:utf-8
# 跟前面个题一样的,只是把res 从 list 改成 set ,里面每个元素使用 tuple
# python 就是这么简单...感觉有点没达到训练的目的
# todo 下次重写
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        llen = len(nums)
        res = set([()])
        if not llen:
            return [[]]
        nums.sort()
        self.helper(nums, llen, 0, [], res)
        return [list(_) for _ in res]

    def helper(self, nums, llen, index, cur, res):
        for i in xrange(index, llen):
            cur.append(nums[i])
            res.add(tuple([_ for _ in cur]))
            self.helper(nums, llen, i+1, cur, res)
            cur.pop()

print Solution().subsetsWithDup([])
