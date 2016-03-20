# coding:utf-8
# 合并两个有序数组，num1有足够的空间存放数组
# 很简单，从后面往前面合并就是

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in xrange(n):
                nums1[i] = nums2[i]
            return
        if n == 0:
            return
        pos = m + n - 1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[pos] = nums1[m-1]
                m -= 1
            else:
                nums1[pos] = nums2[n-1]
                n -= 1
            pos -= 1
        if m:
            while m > 0:
                nums1[pos] = nums1[m-1]
                m -= 1
                pos -= 1
        if n:
            while n > 0:
                nums1[pos] = nums2[n-1]
                n -= 1
                pos -= 1

a=[0,1,2,0]
b=[1]
Solution().merge(a, 3, b, 1)
print a