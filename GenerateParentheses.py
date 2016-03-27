# coding:utf-8
# 递归 + 回溯
# 输入 n ,返回 n 对匹配的括号
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        tmp_str = []
        left, right = 0, 0
        if not n:
            return res
        self.helper(res, tmp_str, n, left, right, )
        return res

    def helper(self, res, tmp_str, n, left, right):
        if left < n:
            tmp_str.append('(')
            self.helper(res, tmp_str, n, left + 1, right)
            tmp_str.pop()
        if right < left:
            tmp_str.append(')')
            self.helper(res, tmp_str, n, left, right+1)
            tmp_str.pop()
        if left == n and right == n:
            res.append(''.join(tmp_str))

print Solution().generateParenthesis(3)
