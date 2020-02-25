'''
# File: getAllElements.py
# Author: 0HP
# Date: 20200223
# Purpose: solve the problem in website: 
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Inorder(self,root:TreeNode,l:list):
        if root==None:
            return
        self.Inorder(root.left,l)
        l.append(root.val)
        self.Inorder(root.right,l)
    def MergeSort(self,l1:list,l2:list):
        l1size,l2size=len(l1),len(l2)
        result=[]
        i,j=0,0
        while i<l1size and j<l2size:
            if l1[i]<l2[j]:
                result.append(l1[i])
                i+=1
            else:
                result.append(l2[j])
                j+=1
        while i<l1size:
            result.append(l1[i])
            i+=1
        while j<l2size:
            result.append(l2[j])
            j+=1
        return result
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        r1,r2=[],[]
        self.Inorder(root1,r1)
        self.Inorder(root2,r2)
        return self.MergeSort(r1,r2)
