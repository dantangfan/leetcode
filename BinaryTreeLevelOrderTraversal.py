# coding: utf-8
# 求二叉树的每层，广度优先遍历，用队列
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = []  # (depth, node)
        queue.append((0, root))
        res = []
        llen = 0
        while queue:
            depth, node = queue.pop(0)
            if llen <= depth:
                res.append([])
                llen += 1
            res[depth].append(node.val)
            if node.left:
                queue.append((depth+1, node.left))
            if node.right:
                queue.append((depth+1, node.right))
        return res

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = []  # (depth, node)
        queue.append((0, root))
        res = []
        while queue:
            depth, node = queue.pop(0)
            try:
                res[depth].append(node.val)
            except:
                res.append([])
                res[depth].append(node.val)
            if node.left:
                queue.append((depth+1, node.left))
            if node.right:
                queue.append((depth+1, node.right))
        return res
