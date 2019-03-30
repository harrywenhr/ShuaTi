https://leetcode.com/problems/wildcard-matching/


if last char in p is ? or equal
str length
match(m-1,n-1)
if last char in p is *
use as multiple
match(m-1,n)
use as one
match(m-1,n - 1)
use as 0
match(m, n - 1)

match(0,0) = True
match(x,0) = False
match(0,x) need to check if all x is *

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dpTable = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        
        for m in range(len(dpTable)):
            for n in range(len(dpTable[0])):
                if m == n == 0:
                    dpTable[0][0] = True
                #if n = 0, we always false except m=n=0
                elif n > 0:
                    if p[n - 1] != "*":
                        if m > 0:
                            if p[n-1] == s[m-1] or p[n-1] == "?":
                                dpTable[m][n] = dpTable[m - 1][n - 1]
                    else:
                        #three case here
                        if m > 0:
                            dpTable[m][n] = dpTable[m][n - 1] or dpTable[m - 1][n - 1] or dpTable[m - 1][n]
                        else:
                            dpTable[m][n] = dpTable[m][n - 1]
        return dpTable[-1][-1]
