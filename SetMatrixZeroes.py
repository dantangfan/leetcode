# coding:utf-8
# 把矩阵中出现0的位置,横竖都标记为0,标记为0跟原始为0是不一样的
# 首先想到的是用 m + n 两个 list 来记录那些行列需要清零,这很容易实现
# 题目要求用 O(1) 的空间,所以,我们可以把位置记录在第一行和第一列上面
# 然后这里就要小心第一行和第一列本来的值
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        x = len(matrix)
        y = len(matrix[0])

        # 判断第0行和第0列是否本来就有0
        x0 = False
        for i in xrange(x):
            if matrix[i][0] == 0:
                x0 = True
                break
        y0 = False
        for j in xrange(y):
            if matrix[0][j] == 0:
                y0 = True
                break

        # 从第一行和第一列开始,标记所有
        for i in xrange(1, x):
            for j in xrange(1, y):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # 从第一行和第一列开始检查,并行列清零
        for i in xrange(1, x):
            if matrix[i][0] == 0:
                for j in xrange(y):
                    matrix[i][j] = 0
        for j in xrange(1, y):
            if matrix[0][j] == 0:
                for i in xrange(x):
                    matrix[i][j] = 0

        # 最后根据原来的判断,来决定首行列是否清零
        if x0:
            for i in xrange(x):
                matrix[i][0] = 0
        if y0:
            for j in xrange(y):
                matrix[0][j] = 0

a = [
    [0,0,0,5],
    [4,3,1,4],
    [0,1,1,4],
    [1,2,1,3],
    [0,0,1,1]
]
a = [[1,1,1],[0,1,2]]
for i in a:
    print i
Solution().setZeroes(a)
print
for i in a:
    print i
# [[0,0,0,0],[0,0,0,4],[0,0,0,0],[0,0,0,3],[0,0,0,0]]