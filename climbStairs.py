'''
# File: climbStairs.py
# Author: 0HP
# Date: 20200203
# Purpose: solve the problem in website: https://leetcode.com/problems/climbing-stairs/
'''

class Solution:
    def Qmul(self,a: int,b: int):
        result=0
        while b:
            if b&1:#b's last bit is 1
                result+=a
            b=b>>1#b=b/2
            a=a<<1#a=a*2
        return result

    def MatrixMul(self,a: [[]],b: [[]]):
        #row of b = col of a
        Arow,Brow,Bcol=2,2,2
        c=[[0,0],[0,0]]

        for i in range(2):
            for j in range(2):
                c[i][j]=self.Qmul(a[i][0],b[0][j])+self.Qmul(a[i][1],b[1][j])

        return c
    def MatrixPow(self,a: [[]],b: int):
        result=[[1,0],[0,1]]
        while b:
            if b&1:
                result=self.MatrixMul(result,a)
            b=b>>1
            a=self.MatrixMul(a,a)
        return result

    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        A=[[1,1],[1,0]]
        F=[[2],[1]]
        A=self.MatrixPow(A,n-2)
        result=self.Qmul(A[0][0],F[0][0])+self.Qmul(A[0][1],F[1][0])
        return result

t=Solution()
print(t.climbStairs(6))

