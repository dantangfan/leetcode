# coding:utf-8
# 判断数独的初始局面是否合法，未填充的数字用 . 表示
# 数独的规则是横、竖、九宫格都必须包含1~9这9个数字
# 1.横、竖、九宫格分三次扫描解答

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        llen = len(board)
        for i in xrange(llen):
            line = [0] * 10
            for j in xrange(llen):
                if board[i][j] != '.':
                    if line[board[i][j]]:
                        return False
                    line[board[i][j]] = 1

        for i in xrange(llen):
            col = [0] * 10
            for j in xrange(llen):
                if board[j][i] != '.':
                    if col[board[j][i]]:
                        return False
                    col[board[j][i]] = 1


# 擦，不喜欢做这个题