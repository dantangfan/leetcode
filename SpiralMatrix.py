# coding: utf-8
# 打印环形矩阵,每次大循环都打印一个圈
#
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        end_Y = len(matrix)
        if not end_Y:
            return []
        end_X = len(matrix[0])
        res = []
        end_X, end_Y = end_X-1, end_Y-1
        cur_X, cur_Y = 0, 0
        while 1:
            for i in xrange(cur_X, end_X+1):
                res.append(matrix[cur_Y][i])
            cur_Y += 1
            if cur_Y > end_Y:
                break
            for i in xrange(cur_Y, end_Y+1):
                res.append(matrix[i][end_X])
            end_X -= 1
            if end_X < cur_X:
                break
            for i in xrange(end_X, cur_X-1, -1):
                res.append(matrix[end_Y][i])
            end_Y -= 1
            if end_Y < cur_Y:
                break
            for i in xrange(end_Y, cur_Y-1, -1):
                res.append(matrix[i][cur_X])
            cur_X += 1
            if cur_X > end_X:
                break
        return res

a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print Solution().spiralOrder(a)


