# coding:utf-8
# 判断给定单词能否在指定矩阵中找到,单词的开头可以在矩阵的任意位置,每个位置只能走一次,可以上下左右走
# 又是一个递归回溯的问题,稍微想想就清楚了
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        x = len(board)
        if not x:
            return False
        y = len(board[0])
        llen = len(word)
        origin = [[_ for _ in b] for b in board]
        for i in xrange(x):
            for j in xrange(y):
                if board[i][j] == word[0]:
                    if self.dfs(board, origin, word, x, y, i, j, llen, 0):
                        return True
        return False

    def dfs(self, board, origin, word, x, y, cur_x, cur_y, llen, index):
        if index == llen:
            return True
        if cur_x >= x or cur_x < 0 or cur_y >= y or cur_y < 0:
            return False
        if origin[cur_x][cur_y] != word[index]:
            return False
        else:
            origin[cur_x][cur_y] = '#'
            res = self.dfs(board, origin, word, x, y, cur_x+1, cur_y, llen, index+1) or\
                  self.dfs(board, origin, word, x, y, cur_x-1, cur_y, llen, index+1) or\
                  self.dfs(board, origin, word, x, y, cur_x, cur_y+1, llen, index+1) or\
                  self.dfs(board, origin, word, x, y, cur_x, cur_y-1, llen, index+1)
            origin[cur_x][cur_y] = board[cur_x][cur_y]
            return res


a = [
  #['A','B','C','E'],
  #['S','F','C','S'],
  ['A','D','E','E']
]

print Solution().exist(a, 'D')