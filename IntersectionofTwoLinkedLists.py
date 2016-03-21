# coding:utf-8
# 查找两个链表的脚垫
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        lena, lenb = 0, 0
        rheada, rheadb = headA, headB
        while rheada:
            lena += 1
            if rheada.next is None:
                lasta = rheada
                break
            rheada = rheada.next
        while rheadb:
            lenb += 1
            if rheadb.next is None:
                lastb = rheadb
                break
            rheadb = rheadb.next
        if lasta != lastb:
            return None
        diff = lena - lenb
        if diff > 0:
            for i in xrange(diff):
                headA = headA.next
        else:
            for i in xrange(-diff):
                headB = headB.next
        while True:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
