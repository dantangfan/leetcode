# coding:utf-8
# 用 logn 的复杂度找出给定排序好数组中指定数字的位置范围
# 二分查找
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []
        llen = len(nums)
        tl, tr = -1, -1
        left, right = 0, llen - 1
        while left <= right:
            mid = left + (right - left)/2
            if nums[mid] == target and (mid == 0 or (mid > 0 and nums[mid - 1] < target)):
                    tl = mid
                    left = mid + 1

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        left, right = 0, llen - 1
        while left <= right:
            mid = left + (right - left)/2
            if nums[mid] == target and (mid == llen - 1 or (mid < llen - 1 and nums[mid + 1] > target)):
                    tr = mid
                    right = mid - 1

            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [tl, tr]

print Solution().searchRange([5, 7, 7, 8, 8, 10], 7)