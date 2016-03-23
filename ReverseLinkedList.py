# coding:utf-8
# 链表翻转
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        right = head.next
        head.next = None
        while right:
            tmp = right
            right = right.next
            tmp.next = head
            head = tmp
        return head