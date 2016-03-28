# coding:utf-8
# 找到一个数插入的到一个数组中的正确位置,如果这个数存在,则返回这个位置
# 二分查找,用一个 flag 来记录上次操作是大于还是小于
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        llen = len(nums)
        left, right = 0, llen - 1
        flag = 0
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                flag = -1
                left = mid + 1
            else:
                flag = 1
                right = mid - 1
        if flag == -1:
            return left
        if flag == 1:
            if right < 0:
                return 0
            else:
                return left

s = Solution()
print s.searchInsert([1,3,5,6], 5)
print s.searchInsert([1,3,5,6], 2)
print s.searchInsert([1,3,5,6], 7)
print s.searchInsert([1,3,5,6], 0)