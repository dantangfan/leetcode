# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q:
            return None
        if p.val > q.val:
            big = p
            small = q
        else:
            big = q
            small = p
        tmp = root
        while tmp:
            if small.val <= tmp.val <= big.val:
                return tmp
            if tmp.val > big.val:
                tmp = tmp.left
            else:
                tmp = tmp.right
        return None