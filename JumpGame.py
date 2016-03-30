class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        llen = len(nums)
        if llen < 2:
            return True
        stack = []
        indexs = set()
        indexs.add(0)
        stack.append(0)
        while stack:
            index = stack.pop()
            jump = nums[index]
            if index + jump >= llen - 1:
                return True
            for i in xrange(1, jump+1):
                tmp = index + i
                if tmp in indexs:
                    continue
                else:
                    stack.append(tmp)
                    indexs.add(tmp)
        return False

print Solution().canJump([2,3,1,1,4])
print Solution().canJump([3,2,1,0,4])
print Solution().canJump([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
print Solution().canJump([2,5,0,0])
print Solution().canJump([10,9,8,7,6,5,4,3,2,1,0,0])

# todo 动态规划,做不来

