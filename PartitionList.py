# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        small = ListNode(-1)
        big = ListNode(-1)
        rsmall, rbig = small, big
        while head:
            if head.val < x:
                rsmall.next = head
                rsmall = rsmall.next
            else:
                rbig.next = head
                rbig = rbig.next
            head = head.next
        rsmall.next = big.next
        rbig.next = None
        return small.next

a = ListNode(1)
b = ListNode(4)
c = ListNode(3)
d = ListNode(2)
e = ListNode(5)
f = ListNode(2)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

res = Solution().partition(a, 3)
while res:
    print res.val
    res = res.next
