# coding:utf-8
# 从数组中移除指定元素，并返回移除之后的长度，没有额外的空间来方数组
# 直接把不是指定元素往前面放就行了

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pos = -1
        l = len(nums)
        for i in xrange(l):
            if val != nums[i]:
                pos += 1
                nums[pos] = nums[i]
        return pos + 1


class Solution(object):
    # 这个的速度要比上一个慢非常多，生成器简直太牛逼
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pos = -1
        for n in nums:
            if val != n:
                pos += 1
                nums[pos] = n
        return pos+1

print Solution().removeElement([2,3,2,2,3,2,4], 2)
