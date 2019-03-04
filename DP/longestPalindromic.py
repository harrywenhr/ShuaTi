https://leetcode.com/problems/longest-palindromic-substring/

dp[k][i] = if is palindromic with length k start at index x 
dp[k][i] = if dp[k - 2][i+1] and str[i] == str[i + k - 1] else False

dp[0][i] all False
dp[1][i] all True
dp[2][i] compare str[i] and str[i + 1]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[None for i in range(len(s))] for k in range(len(s) + 1)]
        maxSub = [0,0]
        for k in range(len(dp)):
            for i in range(len(s)):
                if k == 0:
                    dp[k][i] = False
                elif k == 1:
                    dp[k][i] = True
                elif k == 2:
                    dp[k][i] = s[i] == s[i + 1] if (i + 1)< len(s) else False
                else:
                    compareIndex = i + k - 1
                    if compareIndex < len(s):
                        dp[k][i] = dp[k - 2][i + 1] and s[compareIndex] == s[i]
                    else:
                        dp[k][i] = False
                if dp[k][i]:
                    if k > maxSub[0]:
                        maxSub = [k, i]
        #print(dp)
        res = s[maxSub[1]:maxSub[1] + maxSub[0]]
        return res



#use center to expand, we have 2n - 1 center
#aabb -> center 0,0.5,1,1.5,2,2.5,3 = 7 center
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if len(s) <= 1:
            return s
        resP = [0,0]
        for x in range(2*n - 1):
            centerP = x * 0.5
            pAtCenter = self.findPalineWithCenter(s, centerP)
            if pAtCenter[0] > -1:
                length = pAtCenter[1] - pAtCenter[0] + 1
                #we update the larger palindrom
                if length > (resP[1] - resP[0]):
                    resP = pAtCenter
        return s[resP[0]:resP[1] + 1]


    def findPalineWithCenter(self, s, centerP):
        remainder = centerP % 1
        leftI = centerP - 1 if remainder == 0 else centerP
        rightI = centerP + 1
        leftI = int(leftI)
        rightI = int(rightI)
        if leftI < 0:
            #return start and end of palindrome
            return [0,0]
        if rightI >= len(s):
            return [len(s) - 1, len(s) - 1]
        #if result is -1, means no palindrom with current center
        finalL = finalR = -1
        while leftI >= 0 and rightI < len(s):
            if s[leftI] == s[rightI]:
                finalL = leftI
                finalR = rightI
                leftI -= 1
                rightI += 1
            else:
                break
        return [finalL, finalR]

