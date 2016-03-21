# coding:utf-8
# 求最多能装多少水
# 从两边往中间装，每次去掉短的那块板
# 我也不知道为什么`
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        count = 0
        start, end = 0, len(height) - 1
        while start < end:
            cur = (end - start) * min(height[start], height[end])
            if cur > count:
                count = cur
            if height[end] > height[start]:
                start += 1
            else:
                end -= 1
        return count