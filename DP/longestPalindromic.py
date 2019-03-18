https://leetcode.com/problems/longest-palindromic-substring/



http://windliang.cc/2018/08/05/leetCode-5-Longest-Palindromic-Substring/


dp[k][i] = if is palindromic with length k start at index i 
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

c b c b c 


0  1  2  3  4  5  6  7  8  9  10 11 12
^  #  c  #  b  #  c  #  b  #  c  #  $
0  0  1  0  3  0  5  0  3  0  1  0  0



0  1  2  3  4  5  6  7  8  9  10 11 12
^  #  b  #  a  #  b  #  a  #  d  #  $
0  0  1  0  3  0  3  0  1  0  1  0  0




#Manacher algrithm
https://segmentfault.com/a/1190000008484167
http://windliang.cc/2018/08/05/leetCode-5-Longest-Palindromic-Substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #store result starting index and length
        res = [0,0]
        processedStr = '^'
        for i in range(len(s)):
            processedStr += '#' + s[i]
        processedStr += '#' + '$'
        #p[i] = radius of palindrom centered at processedStr[i], not including index i, so the total length of palindrom
        #is 2 * p[i] + 1, and the length of palindrom in original str is p[i] with start index (i - p[i] ) // 2
        #we return [(i - p[i] ) // 2, (i - p[i] ) // 2 + p[i]]
        p =  [0] * len(processedStr)
        currentCenter = 0
        currentEnd = 0
        #i_mirror = 2 * C - i;
        for i in range(2, len(processedStr)):
            #we can not use previous calculated p, we expand from center i
            if i >= currentEnd:
                radius = self.expandFromCenter(processedStr, i)
                newEnd = i + radius
                p[i] = radius
                if newEnd > currentEnd:
                    currentEnd = newEnd
                    currentCenter = i
            else:
                i_mirror = 2 * currentCenter - i
                #ideally p[i] = p[i_mirror], but we have 3 cases
                #case 1, p[i_mirror] expands outside the current palindrom center at currentCenter
                #p[i] can only be ganrangtee to be currentEnd - i
                if p[i_mirror] > (currentEnd - i):
                    p[i] = currentEnd - i
                elif p[i_mirror] < (currentEnd - i):
                    #case2, p[i_mirror] lies within the current palindrom center at currentCenter
                    p[i] = p[i_mirror]
                else:
                    #case3, p[i_mirror] just reached the end, p[i] >= p[i_mirror], we try to expand
                    currentRadius = p[i_mirror]
                    while ((i - currentRadius - 1) >= 0 and (i + currentRadius + 1) < len(processedStr) and processedStr[i - currentRadius - 1] == processedStr[i + currentRadius + 1]):
                        currentRadius += 1
                    p[i] = currentRadius
                    #update new center
                    newEnd = i + p[i]
                    if newEnd > currentEnd:
                        currentCenter = i
                        currentEnd = newEnd
            if p[i] > res[1]:
                newStartIndex = (i - p[i]) // 2
                res[0] = newStartIndex
                res[1] = p[i]

        print(p)
        return s[res[0]:res[0] + res[1]]

    def expandFromCenter(self, s, centerP):
        left = centerP - 1
        right = centerP + 1
        radius = 0
        while (left >= 0 and right < len(s)):
            if s[left] != s[right]:
                return radius
            left -= 1
            right += 1
            radius += 1
        return radius