# coding:utf-8
# 去除链表中有重复的项
# 一个循环判断当前连续的项是否有重复,直到不重复
# FIXME 早上起来不适宜写代码, 还是晚上爽
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
        if not head or not head.next:
            return head
        rhead = ListNode(-1)
        rhead.next = head
        pre, now = rhead, head
        while now and now.next:
            if now.val == now.next.val:
                while now.next and now.val == now.next.val:
                    now = now.next
                pre.next = now.next
                now = now.next
            else:
                pre = now
                now = now.next
        return rhead.next


a = ListNode(1)
b = ListNode(1)
c = ListNode(1)
d = ListNode(2)
e = ListNode(3)
a.next = b
b.next = c
c.next = d
d.next = e

res = Solution().deleteDuplicates(a)

while res:
    print res.val
    res = res.next
