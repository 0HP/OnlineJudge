'''
# File: invertTree.py
# Author: 0HP
# Date: 202002117
# Purpose: solve the problem in website: https://leetcode.com/problems/invert-binary-tree/
'''
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def invertTree(self, root: TreeNode) -> TreeNode:

        if root==None:
            return None

        root.left,root.right=root.right,root.left

        if not root.left==None:
            root.left=self.invertTree(root.left)

        if not root.right==None:
            root.right=self.invertTree(root.right)

        return root