# coding:utf-8
# 下一个字典序
# 对当前排列从 [后向前扫] 描，找到一对为升序的相邻元素，记为i和j（i < j）。
# 如果不存在这样一对为升序的相邻元素，则所有排列均已找到，算法结束；
# 否则，重新对当前排列从 [后向前扫] 描，找到第一个大于i的元素k，交换i和k，
# 然后对从j开始到结束的子序列反转，则此时得到的新排列就为下一个字典序排列。
# 这种方式实现得到的所有排列是按字典序有序的，这也是C++ STL算法next_permutation的思想。

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        llen = len(nums)
        if llen < 2:
            return
        i, j = llen-2, llen-1
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1
        if i < 0:
            nums.reverse()
            return
        k = llen - 1
        while nums[i] >= nums[k]:
            k -= 1
        nums[i], nums[k] = nums[k], nums[i]
        l = llen - 1
        while j < l:
            nums[j], nums[l] = nums[l], nums[j]
            j += 1
            l -= 1

a = [5, 1, 1]
Solution().nextPermutation(a)
print a



