/**
 * Definition for a binary tree node.*/
#include<stdio.h>
#include<stdbool.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
bool isValidBST(struct TreeNode* root) {
  if(root==NULL) return true;
  struct TreeNode* p;
  if(root->left!=NULL)
  {
    if(root->left->val>=root->val){return false;}
    p=root->left;
    while(p->right!=NULL)
    {p=p->right;}
    if(p->val>=root->val) return false;
  }
  if(root->right!=NULL)
  {
    if(root->right->val<=root->val){return false;}
    p=root->right;
    while(p->left!=NULL)
    {
      p=p->left;
    }
    if(p->val<=root->val) return false;
  }
  if(isValidBST(root->left)==false){return false;}
  if(isValidBST(root->right)==false){return false;}
  return true;
}
