class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        llen = len(nums)
        pos = llen
        for i, v in enumerate(nums):
            if v == 0:
                pos = i
                break
        for i in range(pos+1, llen):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], 0
                pos += 1

a = [3, 1, 1, 3, 12]
Solution().moveZeroes(a)
print a