/*
*File:mergeTrees.c:
*Author:0HP
*Date:20200222
*Purpose:to solve the problem in Leetcode
*https://leetcode.com/problems/merge-two-binary-trees/
*/
#include<stdio.h>
#include<stdlib.h>
struct TreeNode {
  int val;
  struct TreeNode *left;
  struct TreeNode *right;
};

void merge(struct TreeNode* t1,struct TreeNode* t2)
{
  //当前节点求和
  t1->val=t1->val+t2->val;
  //叶子结点，求和返回
  if(t2->left==NULL&&t2->right==NULL)
  {return;}

  if(t1->left!=NULL&&t2->left!=NULL)
  {merge(&(*t1->left),&(*t2->left));}

  if(t1->right!=NULL&&t2->right!=NULL)
  {merge(&(*t1->right),&(*t2->right));}

  //t1无左子树，t2有左子树
  if(t1->left==NULL&&t2->left!=NULL)
  {
    t1->left=t2->left;
  }

  //t1无右子树，t2有右子树
  if(t1->right==NULL&&t2->right!=NULL)
  {
    t1->right=t2->right;
  }
}
struct TreeNode* mergeTrees(struct TreeNode* t1, struct TreeNode* t2){
  if(t1==NULL){return t2;}
  if(t2==NULL){return t1;}
  merge(&(*t1),&(*t2));
  return t1;
}
