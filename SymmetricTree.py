# coding:utf-8
# 判断二叉树是否对称
# 轴对称的二叉树有 left.left == right.right and left.right == right.left
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.cmp(root.left, root.right)

    def cmp(self, left, right):
        if left is not None and right is not None:
            if left.val == right.val:
                return self.cmp(left.left, right.right) and self.cmp(left.right, right.left)
            else:
                return False
        elif left is None and right is None:
            return True
        else:
            return False