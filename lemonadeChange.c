/*
*File:lemonadeChange.c:
*Author:0HP
*Date:20200202
*Purpose:to solve the problem in Leetcode
*https://leetcode.com/problems/lemonade-change/
*/

/**
*input a array, which is the money, only include 5,10,20
*Output whether we can return the charge
**/

#include<stdio.h>
#include<stdbool.h>
bool lemonadeChange(int* bills, int billsSize){
  int five=0,ten=0;
  for(int i=0;i<billsSize;++i)
  {
    if(bills[i]==5)
    {++five;}
    else if(bills[i]==10)
    {
      --five;
      if(five<0){return false;}
      else{++ten;}
    }
    else
    {
      if(ten>0){--ten;--five;}
      else{five-=3;}
      if(ten<0||five<0){return false;}
    }
  }
  return true;
}
//test
int main ()
{
  int a[5]={5,5,10,10,20};
  printf("%d",lemonadeChange(a,5));
}
