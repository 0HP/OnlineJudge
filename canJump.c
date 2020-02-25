/*
*File:canJump.c:
*Author:0HP
*Date:20200224
*Purpose:to solve the problem in Leetcode
*https://leetcode.com/problems/jump-game/
*/
#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
bool canJump(int* nums, int numsSize)
{
  if(numsSize==0)return false;
  if(numsSize==1)return true;

  int temp=0;
  for(int i=0;i<=temp;++i)
  {
    if(temp<nums[i]+i)
    {temp=nums[i]+i;}
    if(temp>=(numsSize-1)){return true;}
  }
  return false;
}
