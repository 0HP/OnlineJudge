/*
*File:searchBST.c
*Author:0HP
*Date:20200216
*Purpose:to solve the problem in Leetcode
*https://leetcode.com/problems/search-in-a-binary-search-tree/
*/
#include<stdio.h>
#include<stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
struct TreeNode* searchBST(struct TreeNode* root, int val)
{
  if(root==NULL){return NULL;}
  else
  {
    if(val<root->val)
    {return searchBST(&(*root->left),val);}
    else if(val>root->val)
    {return searchBST(&(*root->right),val);}
    else
    {
      return &(*root);
    }
  }
}
