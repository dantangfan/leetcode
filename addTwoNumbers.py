# coding:utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 本题就是一个简单地链表大数加法，连翻转都不用。
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        head = res
        tmp = 0
        while tmp or l1 or l2:
            # 要注意l1,12只有n位时，res有n+1位的情况
            node = ListNode(tmp)
            if l1:
                node.val += l1.val
                l1 = l1.next
            if l2:
                node.val += l2.val
                l2 = l2.next
            tmp = node.val / 10
            node.val %= 10
            head.next = node
            head = head.next
        return res.next

