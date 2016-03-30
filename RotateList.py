# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        left, right = head, head
        llen = 0
        while head:
            head = head.next
            llen += 1
        k %= llen
        if k == 0:
            return left
        for i in xrange(llen - k - 1):
            right = right.next
        tmp = right
        right = right.next
        tmp.next = None
        tmp = right
        while tmp.next:
            tmp = tmp.next
        tmp.next = left
        return right

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

res = Solution().rotateRight(a, 0)
while res:
    print res.val
    res = res.next

