# coding:utf-8
# 求从左上到右下最小的路径和
# 直接用神搜广搜会超时
# 其实是一个简单的动态规划问题
# res[i][j] = min(res[i-1][j], res[i][j-1]) + grid[i][j]

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        max_x = len(grid) - 1
        max_y = len(grid[0]) - 1
        min_sum = None
        stack = [(0, 0, grid[0][0])]
        while stack:
            x, y, cur = stack.pop()
            if x == max_x and y == max_y:
                if min_sum is None or min_sum > cur:
                    min_sum = cur
            if x < max_x:
                stack.append((x+1, y, cur+grid[x+1][y]))
            if y < max_y:
                stack.append((x, y+1, cur+grid[x][y+1]))
        return min_sum


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        max_x = len(grid)
        max_y = len(grid[0])
        res = [[0]*max_y for i in xrange(max_x)]
        res[0][0] = grid[0][0]
        for i in xrange(max_x):
            for j in xrange(max_y):
                if i == 0 and j != 0:
                    res[i][j] = res[i][j-1] + grid[i][j]
                elif j == 0 and i != 0:
                    res[i][j] = res[i-1][j] + grid[i][j]
                elif i != 0 and j != 0:
                    res[i][j] = min(res[i-1][j], res[i][j-1]) + grid[i][j]
        return res[max_x-1][max_y-1]
a = [
    [0,0,0],
    [-1,0,0],
    [0,-1,0]
]
print Solution().minPathSum(a)
