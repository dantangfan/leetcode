# coding:utf-8
# 很经典的问题
# 从 右上角 开始匹配
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        x = len(matrix) - 1
        y = len(matrix[0]) - 1
        i, j = 0, y
        while i <= x and j >=0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

a = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

print Solution().searchMatrix(a, 51)