# coding:utf-8
# 删除有序数组的重复元素，并返回最终的长度
# 多简单的事情，直接set就完了，然而，题目说了，这里没有额外的空间
# 记录一个位置，从这个位置之前的都是不重复的数字，后面的不重复的数字往前面方就行了

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        pos = 0
        l = len(nums)
        for i in xrange(1, l):
            if nums[pos] != nums[i]:
                pos += 1
                nums[pos] = nums[i]
        return pos+1

print Solution().removeDuplicates([])

