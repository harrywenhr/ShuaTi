https://leetcode.com/problems/edit-distance/

Given two words word1 and word2, find the minimum number of operations
 required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

dp(m,n) means steps from substr length m to substr length n
dp(m,n) = 
1. if str[m - 1] == str[ n-1], dp(m-1, n - 1)
#either we insert, delete or modify
2. min (dp(m - 1, n), dp(m, n - 1), dp(m-1, n -1)) + 1

basecase
dp(0,0) = 0
dp(m,0) = m
dp(0,n) = n
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #we use length as different positions
        dpTable = [[0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
        for i in range(len(word2) + 1):
            for j in range(len(word1) + 1):
                if i == 0:
                    dpTable[i][j] = j
                elif j == 0:
                    dpTable[i][j] = i
                else:
                    if word2[i - 1] == word1[j - 1]:
                        dpTable[i][j] = dpTable[i - 1][j - 1]
                    else:
                        dpTable[i][j] = min(dpTable[i - 1][j - 1], dpTable[i - 1][j], dpTable[i][j - 1]) + 1
        return dpTable[-1][-1]