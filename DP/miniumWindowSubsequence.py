
class Solution:


#two pointer, when a match found, we start from reverse to optimise it, and when find a optimal start i, we restart with i + 1, reset j = 0

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        mapT = set(list(T))
        i,j,m,n = 0,0,len(S),len(T),
        #resutlt substring start and length
        res = [-1,sys.maxsize]
        while i < m:
            validStartI = -1
            while i < m and j < n:
                if S[i] == T[j]:
                    j += 1
                i += 1
            if j == n:
                #we have a valid substring, we try to optimise it from backwards
                i -= 1
                j -= 1
                validEndI = i
                #print("{0} {1}".format(validEndI, j))
                while j >= 0:
                    if S[i] == T[j]:
                        j -= 1
                    i -= 1
                    #print("what %d" % i)
                #now we have a valid optimised mataching sub string, we record
                startI = i + 1
                validStartI = startI
                #print(startI)
                length = validEndI - startI + 1
                if length < res[1]:
                    res = [startI, length]
            #we recheck from end + 1
            if validStartI >= 0:
                i = validStartI + 1
                j = 0
        return "" if res[0] == -1 else S[res[0]:res[0] + res[1]]








#sliding window
#left, right index, when a window is matched, move left window till window un qualify, then record data
#continue with right index
    def minWindow(self, S: str, T: str) -> str:
        mapT = set(list(T))
        left = right = 0
        #resutlt substring start and length
        res = [-1,sys.maxsize]
        while right < len(S):
            while self.isSubsequence(S,T,left,right):
                #record current valid window size
                validLength = right - left + 1
                if validLength < res[1]:
                    res = [left, validLength]
                #we have a valid window, we keep increasing left
                left += 1
            #we increase the right index
            right += 1
        return "" if res[0] == -1 else S[res[0]:res[0] + res[1]]


    #check if s2 is a subseqence of s1
    #O(N)
    def isSubsequence(s1, s2, s1Start, s1End):
        i,j = s1Start,0
        while i <= s1End and j <= len(s2):
            if s1[i] == s2[j]:
                j += 1
            i += 1
        return j == len(s2)


dp[i][j] = start index in S that ends at i, which contains end at j in T as subseqence

dp[0][0] = 0 if first char of S == T
if i < j dp[i][j] = -1

dp[i][j] = dp[i - 1][j - 1] if S[i] == T[j] else dp[i - 1][j]
dp[0][0] = 0 if first char of S == T
dp[x][0] = x - 1

each item we have dp[i][n] we record a minLength

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        m,n = len(S), len(T)
        dp = [[-1 for i in range(n)] for j in range(m)]
        res = [-1, sys.maxsize]
        for i in range(m):
            for j in range(n):
                if i >= j:
                    #print("hereA {0} {1}".format(i, j))
                    if S[i] == T[j]:
                        #print("hereB {0} {1}".format(i, j))
                        if i == j == 0:
                            dp[i][j] = 0
                        else:
                            #print("hereC {0} {1}".format(i, j))
                            #if j == 0 then we set start index to i
                            dp[i][j] = dp[i - 1][j - 1] if j >= 1 else i
                    else:
                        dp[i][j] = dp[i - 1][j] if i >= 1 else -1
            #we finished set one row, we get current min length
            currentLength = i - dp[i][n - 1] + 1
            #print(currentLength)
            if currentLength < res[1] and dp[i][n - 1] >= 0:
                res = [dp[i][n - 1], currentLength]
        #print(dp)
        return "" if res[0] == -1 else S[res[0]:res[0] + res[1]]

