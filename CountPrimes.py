# coding:utf-8
# 计算小于n的素数的数量
# 首先抛弃掉所有不会是素数的书,比如2,3,4等的倍数
class Solution(object):
    # 超时了
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        nums = [0] * n
        count = 0
        for i in xrange(2, n):
            if not nums[i]:
                nums[i] = self.is_primes(i)
            else:
                continue
            if nums[i] == 1:
                count += 1
                for j in xrange(2, n):
                    mul = i * j
                    if mul >= n:
                        break
                    nums[mul] = 2
        return count

    def is_primes(self, n):
        for i in xrange(2, n):
            if i * i > n:
                break
            if not n % i:
                return 0
        return 1

class Solution1(object):
    # 去掉不是素数的,剩下的就是素数
    def countPrimes(self, n):
        if n <= 2:
            return 0
        nums = [1] * n
        nums[0], nums[1] = 0, 0
        for i in xrange(2, n):
            if nums[i]:
                for j in xrange(2, (n-1)//i+1):
                    nums[j*i] = 0
        return sum(nums)


print Solution().countPrimes(499979)
