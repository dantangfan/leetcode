# coding:utf-8
# 从列表中删除倒数第n个节点
# 一个指针先走n步，后面指针跟上，前面个指针走完的时候就是第n个节点
# 注意要删除的节点是第一个或者最后一个的情况

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None
        first, second, back = head, head, head
        for i in xrange(n):
            first = first.next
        while first:
            back = second
            second, first = second.next, first.next
        if second == head:
            return head.next
        back.next = second.next
        return head

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

head = c

while c:
    print c.val
    c = c.next

d = Solution().removeNthFromEnd(head, )

while d:
    print d.val
    d = d.next
