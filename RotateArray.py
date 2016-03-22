class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        k %= len(nums)
        for i in xrange(k):
            n = nums.pop()
            nums.insert(0, n)

print Solution().rotate([1,2,3,4,5,6,7], 1)