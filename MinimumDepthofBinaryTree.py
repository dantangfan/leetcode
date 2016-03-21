# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = []  # (depth, node)
        min_depth = 0
        stack.append((1,root))
        while stack:
            depth, node = stack.pop()
            if not node.left and not node.right:
                if not min_depth:
                    min_depth = depth
                elif min_depth > depth:
                    min_depth = depth
            if node.left:
                stack.append((depth+1, node.left))
            if node.right:
                stack.append((depth+1, node.right))
        return min_depth
