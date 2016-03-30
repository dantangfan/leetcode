# coding:utf-8
# 一个一个的用 next_permutation 超时了
# todo 肯定有数学解法
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 0:
            return ""
        cn, nn = 1, n
        while nn:
            cn *= nn
            nn -= 1
        k %= cn
        if k == 0:
            k = cn
        cur_per = range(1, n+1)
        for i in xrange(k-1):
            self.next_permutation(cur_per, n)
        return ''.join([str(i) for i in cur_per])

    def next_permutation(self, cur_per, size):
        i, j = size-2, size-1
        while i >= 0 and cur_per[i] >= cur_per[j]:
            i -= 1
            j -= 1
        if i < 0:
            return
        k = size - 1
        while cur_per[i] >= cur_per[k]:
            k -= 1
        cur_per[i], cur_per[k] = cur_per[k], cur_per[i]
        l = size - 1
        while j < l:
            cur_per[j], cur_per[l] = cur_per[l], cur_per[j]
            j += 1
            l -= 1

print Solution().getPermutation(8, 40000)