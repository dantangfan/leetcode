# coding:utf-8
# 返回杨辉三角
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if rowIndex < 0:
            return []
        if rowIndex == 0:
            return [1]
        numRows = rowIndex + 1
        res = [[1]]
        for i in xrange(1, numRows):
            tmp = [1]
            for j in xrange(1, i):
                tmp.append(res[i-1][j-1] + res[i-1][j])
            tmp.append(1)
            res.append(tmp)
        return res[rowIndex]

print Solution().getRow(4)