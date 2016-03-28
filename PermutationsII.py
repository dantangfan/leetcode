class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        llen = len(nums)
        if llen < 2:
            return [nums]
        res = []
        while self.next_permute(nums, llen):
            tmp = [_ for _ in nums]
            res.append(tmp)
        return res

    def next_permute(self, nums, llen):
        left, right = llen-2, llen-1
        while left >= 0 and nums[left] >= nums[right]:
            left -= 1
            right -= 1
        if left < 0:
            return False
        k = llen - 1
        while nums[left] >= nums[k]:
            k -= 1
        nums[left], nums[k] = nums[k], nums[left]
        l = llen - 1
        while right < l:
            nums[right], nums[l] = nums[l], nums[right]
            right += 1
            l -= 1
        return True
s = Solution()
a = [1, 1]
print s.permuteUnique(a)