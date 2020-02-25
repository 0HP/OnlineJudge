'''
# File: hasPathSum.py
# Author: 0HP
# Date: 20200217
# Purpose: solve the problem in website: https://leetcode.com/problems/path-sum/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def RecordPath(self,root:TreeNode,sum:int,sumlist:list):

        if root==None:
            return

        sum=sum+root.val

        if root.left==None and root.right==None:
            sumlist.append(sum)

        self.RecordPath(root.left,sum,sumlist)
        self.RecordPath(root.right,sum,sumlist)


    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        Sum=0
        Sumlist=[]

        self.RecordPath(root,Sum,Sumlist)

        for i in sumlist:
            if sum==i:
                return True

        return False
