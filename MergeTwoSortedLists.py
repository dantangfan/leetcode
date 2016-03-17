# coding:utf-8
# 链表合并，并没有说明是升序还是降序，这里默认好像是升序
# 1.直接对两个链表每个元素依次操作

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)
        nhead = head
        while l1 and l2:
            if l1.val < l2.val:
                nhead.next = l1
                nhead, l1 = nhead.next, l1.next
            else:
                nhead.next = l2
                nhead, l2 = nhead.next, l2.next
        if l1:
            nhead.next = l1
        if l2:
            nhead.next = l2
        return head.next

a = ListNode(1)
b, c = a, a
a.next = ListNode(2)
a, b = a.next, a
a.next = ListNode(3)
a, b = a.next, a
a.next = ListNode(4)
a, b = a.next, a
a.next = ListNode(5)
a, b = a.next, a

l1 = c

a = ListNode(1)
b, c = a, a
a.next = ListNode(2)
a, b = a.next, a
a.next = ListNode(3)
a, b = a.next, a
a.next = ListNode(4)
a, b = a.next, a
a.next = ListNode(5)
a, b = a.next, a

l2 = c

res = Solution().mergeTwoLists(l1, l2)

while res:
    print res.val
    res = res.next