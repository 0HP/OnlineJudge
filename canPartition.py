'''
# File: canPartition.py
# Author: 0HP
# Date: 20200204
# Purpose: solve the problem in website: https://leetcode.com/problems/partition-equal-subset-sum/
'''
class Solution:
    def canPartition(self, nums: []) -> bool:
        numcounts=len(nums)
        numsum=sum(nums)
        #if the sum of the list is odd, it must can not be part
        if numsum&1 or numcounts<2:
            return False

        weight=numsum//2

        Bag=[[False for i in range(weight+1)]for i in range(numcounts+1)]

        for i in range(weight+1):
            if nums[0]==i:
                Bag[1][i]=True

        for i in range(2,numcounts+1):
            for j in range(weight+1):
                if not j<nums[i-1]:
                    Bag[i][j]=Bag[i-1][j] or Bag[i-1][j-nums[i-1]]
                else:
                    Bag[i][j]=Bag[i-1][j]

        return Bag[-1][-1]

t=Solution()
l=[1,5,11,5]
print(t.canPartition(l))