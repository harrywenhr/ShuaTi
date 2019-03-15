https://leetcode.com/problems/regular-expression-matching/
#
# mark match(m,n) as 
1 if last char in n is . or last char of m,n is equal
    match(m - 1, n - 1)
  if last char in n is *
    1   if p.charAt(n-1) != s.charAt(m) : dp[n][m] = dp[n - 2][m]  
         //in this case, a* only counts as empty
    2   if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.':
                we can use * 0,1,multiple times

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #let row be pattern str, column be match str
        #need patch one before, length i and length j
        dpTable = [[False for j in range(len(s) + 1)] for i in range(len(p) + 1)]
        for i in range(len(p) + 1):
            for j in range(len(s) + 1):
                emptyStarUsed = dpTable[i - 2][j] if i >= 2 else False
                if i == 0 and j == 0:
                    dpTable[i][j] = True
                elif i == 0:
                    dpTable[i][j] = False
                elif j == 0:
                    dpTable[i][j] = emptyStarUsed and p[i - 1] == '*'
                else:
                    #last char is equal or ., we use one char in pattern
                    if p[i - 1] == '.' or p[i - 1] == s[j - 1]:
                        dpTable[i][j] = dpTable[i - 1][j - 1]
                    elif p[i - 1] == '*':
                        if p[i - 2] == '.' or p[i - 2] == s[j - 1]:
                            #we can use 0,1,or multipe a*
                            #first one is multiple, second one is one * used, third one is empty * used
                            dpTable[i][j] = dpTable[i][j - 1] or dpTable[i - 1][j - 1] or emptyStarUsed 
                        else:
                            #use 0 a*
                            dpTable[i][j] = emptyStarUsed
        return dpTable[-1][-1]





