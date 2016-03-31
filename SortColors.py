# coding:utf-8
# 经典问题
# 排序 0,1,2 三个数字
# 只需要三个指针分别指向头/尾/当前位置,将0向左移,2向右移


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        llen = len(nums)
        if not llen:
            return
        left, right = 0, llen - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            if nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1

a = [1,2,0,0,0,2,2,1,1,0,1]
a = [1, 0]
Solution().sortColors(a)
print a