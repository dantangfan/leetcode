#coding:utf-8
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 由于要返回现有的index，所以不能先排序
        # 有可能有多个数字式重复的，所以也不能直接用把list转为dict
        # 可以从小到大的将list中的数据放入dict，如果存在一个target-i的dict值，那么这个值一定是之前放进去的
        # 复杂度n
        d = {}
        for i in range(len(nums)):
            if d.get(target-nums[i], None) == None:
                d[nums[i]] = i
            else:
                return [d[target-nums[i]]+1, i+1]

s = Solution()
print s.twoSum([0,4,3,0], 0)