# coding:utf-8
# 定点的链表翻转
# 最好也是在最前面定一个头结点
# 然后一遍对链表扫描,分成三段,其中中间段要翻转.最后再拼接起来
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        if m == n:
            return head
        L = ListNode(-1)
        L.next = head
        head = L
        rhead, thead = head, head
        for i in xrange(m-1):
            thead = thead.next
        leftend = thead
        thead = thead.next
        leftend.next = None
        midend, midhead = thead,thead
        thead = thead.next
        midend.next = None
        for i in range(n-m):
            tmp = thead
            thead = thead.next
            tmp.next = midhead
            midhead = tmp
        leftend.next = midhead
        midend.next = thead
        return rhead.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

r = Solution().reverseBetween(a, 1, 1)
while r:
    print r.val
    r = r.next
