/*
*File:numTrees.c:
*Author:0HP
*Date:20200222
*Purpose:to solve the problem in Leetcode
*https://leetcode.com/problems/unique-binary-search-trees/
*/
#include<stdio.h>
#include<stdlib.h>
int numTrees(int n){
  if(n<3){return n;}
  int *a;
  a=(int*)malloc(sizeof(int)*(n+1));
  a[0]=1;a[1]=1;a[2]=2;
  for(int i=3;i<n+1;++i)
  {
    int half=i/2;
    a[i]=0;
    if(i%2==0)
    {
      for(int j=0;j<half;++j)
      {
        a[i]=a[i]+a[i-j-1]*a[j];
      }
      a[i]=a[i]<<1;
    }
    else
    {
      for(int j=0;j<half;++j)
      {
        a[i]=a[i]+a[i-j-1]*a[j];
      }
      a[i]=a[i]*2+a[half]*a[half];
    }
  }
  return a[n];
}

int main ()
{
  printf("%d",numTrees(3));
}
