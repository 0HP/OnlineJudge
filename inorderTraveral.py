'''
# File: inorderTraveral.py
# Author: 0HP
# Date: 20200223
# Purpose: solve the problem in website: 
# https://leetcode.com/problems/binary-tree-inorder-traversal/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def InOrder(self,root:TreeNode,l:list):
        if root==None:
            return
        self.InOrder(root.left,l)
        l.append(root.val)
        self.InOrder(root.right,l)
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        a=[]
        self.InOrder(root,a)
        return a