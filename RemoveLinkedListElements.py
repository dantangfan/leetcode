# coding:utf-8
# 删除链表中指定值的元素
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        rhead = ListNode(-1)
        tmp = rhead
        while head:
            if head.val != val:
                tmp.next = head
                tmp = tmp.next
            head = head.next
        tmp.next = None
        return rhead.next