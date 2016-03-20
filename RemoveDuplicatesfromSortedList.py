# coding:utf-8
# 从排序链表中去处连续重复项
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        left, right = head, head.next

        while right:
            if left.val == right.val:
                left.next = right.next
                right = right.next
            else:
                left = left.next
                right = right.next
        return head
