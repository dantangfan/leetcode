# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if abs(self.depth(root.left, 1) - self.depth(self.right, 1)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root, depth):
        if not root:
            return depth
        return max(self.depth(root.left, depth+1), self.depth(root.right, depth+1))
