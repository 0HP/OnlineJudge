'''
# File: binaryTreePaths.py
# Author: 0HP
# Date: 202002116
# Purpose: solve the problem in website: https://leetcode.com/problems/binary-tree-paths/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def visit(self,root:TreeNode,onepath:str,path:list):
        if root==None:
            return

        onepath=onepath+"->"+str(root.val)
        #找到根节点，即找到一条路径
        if root.left==None and root.right==None:
            path.append(onepath[2:])

        self.visit(root.left,onepath,path)
        self.visit(root.right,onepath,path)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        onepath=""
        paths=[]
        self.visit(root,onepath,paths)

        return paths




