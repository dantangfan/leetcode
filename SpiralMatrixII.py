class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        res = [[0]*n for i in xrange(n)]
        x, y = 0, 0
        max_x, max_y = n-1, n-1
        num = 1
        while True:
            if x > max_x or y > max_y:
                break
            for i in xrange(y, max_y+1):
                res[x][i] = num
                num += 1
            x += 1
            for j in xrange(x, max_x+1):
                res[j][max_y] = num
                num += 1
            max_y -= 1
            for i in xrange(max_y, y-1, -1):
                res[max_x][i] = num
                num += 1
            max_x -= 1
            for j in xrange(max_x, x-1, -1):
                res[j][y] = num
                num += 1
            y += 1
        return res

print Solution().generateMatrix(1)