# coding:utf-8
# 排序好的数组,给出最多可以重复一次的长度
# 直接两个位置来保存当前最后两个数,然后判断后来的数是否跟他们两个都相等


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        llen = len(nums)
        if llen < 3:
            return
        left, right = 0, 1
        for i in xrange(2, llen):
            if nums[i] != nums[right] or nums[i] != nums[left]:
                nums[right+1] = nums[i]
                left, right = right, right+1
        return right + 1

a = [1,1,1,2,2]
print Solution().removeDuplicates(a)