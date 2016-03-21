# coding:utf-8
# 查找数组中出现次数超过一半的数，用一个栈来记录，最终结果就是栈顶值
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        llen = len(nums)
        stack = []
        for i in xrange(llen):
            if stack:
                if nums[i] == stack[-1]:
                    stack.append(nums[i])
                else:
                    stack.pop()
            else:
                stack.append(nums[i])
        return stack[-1]

print Solution().majorityElement([3,2,3,2])