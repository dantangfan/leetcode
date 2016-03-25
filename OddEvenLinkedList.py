# coding:utf-8
# 把链表奇数位放在偶数位前面
# 分别记录奇数和偶数位,然后合并
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        odd, even = ListNode(1), ListNode(2)
        todd, teven = odd, even
        index = 1
        while head:
            if index % 2:
                todd.next = head
                head = head.next
                todd = todd.next
                todd.next = None
            else:
                teven.next = head
                head = head.next
                teven = teven.next
                teven.next = None
            index += 1
        todd.next = even.next
        return odd.next
