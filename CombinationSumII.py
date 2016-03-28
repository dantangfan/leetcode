# coding:utf-8
# 找出数组中所有和为定值的项的集合,一个数字可以多次出现
# 递归 + 回溯
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        res = []
        self.helper(sorted(candidates), target, 0, [], res)
        return res


    def helper(self, array, target, cur_sum, sum, res):
        if cur_sum == target:
            tmp = [_ for _ in sum]
            if tmp not in res:
                res.append(tmp)
            return
        if cur_sum > target:
            return
        for i, a in enumerate(array):
            if cur_sum + a > target:
                break
            cur_sum += a
            sum.append(a)
            self.helper(array[i+1:], target, cur_sum, sum, res)
            cur_sum -= a
            sum.pop()

s = Solution()
print s.combinationSum([1], 8)