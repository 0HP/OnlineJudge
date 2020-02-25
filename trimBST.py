'''
# File: trimBST.py
# Author: 0HP
# Date: 202002117
# Purpose: solve the problem in website: https://leetcode.com/problems/trim-a-binary-search-tree/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:

        if root==None:
            return None

        if root.val<L:
            return self.trimBST(root.right,L,R)

        elif root.val>R:
            return self.trimBST(root.left,L,R)

        else:
            root.left=self.trimBST(root.left,L,R)
            root.right=self.trimBST(roor.right,L,R)
            return root



