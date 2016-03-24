# coding:utf-8
# 深度优先打印二叉树的路径
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        res = []
        nodes = []
        if root:
            self.helper(root, res, nodes)
        return res

    def helper(self, root, res, nodes):
        nodes.append(str(root.val))
        if not root.left and not root.right:
            res.append('->'.join(nodes))
        if root.left:
            self.helper(root.left, res, nodes)
        if root.right:
            self.helper(root.right, res, nodes)
        nodes.pop()
