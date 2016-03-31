# coding:utf-8
# 简单走迷宫问题,一共有多少种方法能从左上角到右下角
# 如果直接使用广搜或者深搜,会超时
# 这也是一个简单的动态规划问题
# res[i][j] = res[i-1][j] + res[i][j-1]
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        max_x = len(obstacleGrid) - 1
        max_y = len(obstacleGrid[0]) - 1
        stack = []
        count = 0
        stack.append((0, 0))
        while stack:
            x, y = stack.pop()
            if x == max_x and y == max_y:
                count += 1
            if x < max_x and obstacleGrid[x+1][y] == 0:
                stack.append((x+1, y))
            if y < max_y and obstacleGrid[x][y+1] == 0:
                stack.append((x, y+1))
        return count


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        max_x = len(obstacleGrid)
        max_y = len(obstacleGrid[0])
        res = [[0]*max_y for i in xrange(max_x)]
        res[0][0] = 1
        for i in xrange(max_x):
            for j in xrange(max_y):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                else:
                    if i > 0:
                        res[i][j] += res[i-1][j]
                    if j > 0:
                        res[i][j] += res[i][j-1]
        return res[max_x-1][max_y-1]


a = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
print Solution().uniquePathsWithObstacles(a)