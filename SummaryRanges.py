class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        start = cur = nums[0]
        llen = len(nums)
        i = 1
        while i < llen:
            if nums[i] == cur + 1:
                cur = nums[i]
            else:
                if cur == start:
                    res.append(str(cur))
                else:
                    res.append(str(start)+'->'+str(cur))
                start = cur = nums[i]
            i += 1
        if cur == start:
            res.append(str(cur))
        else:
            res.append(str(start)+'->'+str(cur))
        return res

print Solution().summaryRanges([0,5,9])