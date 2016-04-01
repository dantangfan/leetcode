# coding: utf-8
# 打印出 k 个 1--n 的数字的所有组合
# 直接使用递归


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []
        res = []
        self.helper(n, k, res, 1, [], 0)
        return res

    def helper(self, n, k, res, start, cur, depth):
        if depth >= k:
            return
        for i in xrange(start, n+1):
            cur.append(i)
            if depth == k-1:
                tmp = [_ for _ in cur]
                res.append(tmp)
            else:
                self.helper(n, k, res, i+1, cur, depth+1)
            cur.pop()

print Solution().combine(4,2)