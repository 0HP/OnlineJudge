'''
# File: minAddToMakeValid.py
# Author: 0HP
# Date: 20200202
# Purpose: solve the problem in website: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
'''

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        Slength=len(S)
        #empty string
        if Slength==0:
            return 0

        index,left,right=0,0,0
        #left meaning "(",need ")"
        #right meaning ")", which can cancel left "(" if it exist before ")"
        while index<Slength:
            #when index not point to the last char
            if index<Slength-1:#if it exist "()"
                if S[index]=='(' and S[index+1]==')':
                    index+=2

                elif S[index]=='(' and S[index+1]=='(':
                    left+=1
                    index+=1
                #when it be ")"
                else:
                    #exist ")",cancel one ")"
                    if left>0:
                        left-=1
                        index+=1
                    #not exist, right+1
                    else:
                        right+=1
                        index+=1
            #the last char
            else:
                if S[index]=='(':
                    left+=1
                    index+=1
                else:
                    if left>0:
                        left-=1
                        index+=1
                    else:
                        right+=1
                        index+=1
        return left+right

t=Solution()
S="()()"
print(t.minAddToMakeValid(S))