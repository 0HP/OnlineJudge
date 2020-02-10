'''
# File: findMaxForm.py
# Author: 0HP
# Date: 202002110
# Purpose: solve the problem in website: https://leetcode.com/problems/ones-and-zeroes/
'''
class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:

        #build the space of bag which has 2 orders
        #row is n,col is m
        dp=[[0 for i in range(n+1)]for j in range(m+1)]

        for i in strs:
            zeros,ones,zero,one=m,n,0,0
            for j in i:
                if j=="1":#"1"'s counts
                    one+=1
                if j=="0":#"0"'s counts
                    zero+=1

            while not zeros<zero:
                ones=n
                while not ones<one:
                    dp[zeros][ones]=max(dp[zeros][ones],dp[zeros-zero][ones-one]+1)
                    ones-=1
                zeros-=1

        return dp[-1][-1]

t=Solution()
print(t.findMaxForm(["10","0001","111001","1","0"],5,3))