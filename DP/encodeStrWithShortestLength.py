https://leetcode.com/problems/encode-string-with-shortest-length/

Either don't encode s at all, or encode it as one part k[...] or encode 
it as multiple parts (in which case we can somewhere split it into two 
    subproblems). Whatever is shortest.

Is O(n) which in worst case happens for every substring of s (O(n^2))

Memoization prevents exponential run time, some substrings may repeat 
but memo will quickly end the recursion

So all in all O(n^3)





class Solution:
    def encode(self, s, memo={}):
        if s not in memo:
            #min is itself for start
            minEncode = s
            n = len(s)
            repeatingBlockSize = (s + s).find(s, 1)
            onePart = s
            #if block size = n, we dont have repeating block
            if repeatingBlockSize < n:
                numberOfBlocks = n // repeatingBlockSize
                #for current repeating block we may be able to encode further
                blockString = self.encode(s[:repeatingBlockSize])
                #blockString = s[:repeatingBlockSize]
                onePart = '%d[%s]' % (numberOfBlocks, blockString)
            if len(onePart) < len(minEncode):
                minEncode = onePart
            for i in range(1, n):
                leftPart = self.encode(s[:i])
                rightPart = self.encode(s[i:])
                multiPart = leftPart + rightPart
                if len(multiPart) < len(minEncode):
                    minEncode = multiPart
            memo[s] = minEncode
        return memo[s]








class Solution:
#for substr length <=4, we dont encode
#sub str length > 5, either we encode whole thing, or encode from
#a[1:i] + a[i:end + 1], we use the shortest

#dp(k, i) = encode for substr with length k start at index i
    def encode(self, s):
        if not s:
            return ""
        n = len(s)
        dp = [["" for i in range(n)] for j in range(n + 1)]
        for k in range(1, n + 1):
            for startI in range(n - k + 1):
                endI = startI + k - 1
                currentSubstr = s[startI:endI + 1]
                #we dont encode
                if k <= 4:
                    dp[k][startI] = currentSubstr
                else:
                    currentMinEncodeStr = currentSubstr
                    #check if we can encode as a whole
                    newS = currentSubstr + currentSubstr
                    repeatingBlockSize = newS.find(currentSubstr, 1)
                    #we can encode our self as a whole via a repeating block
                    if repeatingBlockSize != k:
                        encodeNumber = k // repeatingBlockSize
                        #blockString = currentSubstr[:repeatingBlockSize]
                        blockString = dp[repeatingBlockSize][startI]
                        encodeStr = "%d[%s]" % (encodeNumber, blockString)
                        currentMinEncodeStr = min(currentMinEncodeStr, encodeStr, key = len)
                    #or we try to encode as left and right part

                    for i in range(startI + 1, endI + 1):
                        leftLength = i - startI
                        rightLength = endI - i + 1
                        leftPart = dp[leftLength][startI]
                        rightPart = dp[rightLength][i]
                        multiEncodeStr = leftPart + rightPart
                        currentMinEncodeStr = min(currentMinEncodeStr, multiEncodeStr, key = len)
                    dp[k][startI] = currentMinEncodeStr
        return dp[-1][0]

