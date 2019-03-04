https://leetcode.com/problems/minimum-window-substring/

use sliding window 
2 pointers
check unmatached characters

https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problemsrs5qrrrrdo0k

#One thing needs to be mentioned is that when asked to find maximum substring, we should update maximum after the inner while loop to guarantee that the substring is valid.
# On the other hand, when asked to find minimum substring, we should update minimum inside the inner while loop.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        strMap = {}
        #number in strMap means unmatached character number for current checking window
        for i in range(len(t)):
            strMap[t[i]] = strMap[t[i]] + 1 if t[i] in strMap else 1
        resultStrPosition = [-1,sys.maxsize]
        start = end = 0
        #number of unmatached characters in current window, before we start, all characters is unmatached
        unmatchedCount = len(t)
        while end < len(s):
            #we have a match in current unmatached characters
            if s[end] in strMap:
                if strMap[s[end]] > 0:
                    #reduce the unmatchedCount
                    unmatchedCount -= 1
                #negative number means over matached characters in current window
                strMap[s[end]] -= 1
            #if current window is a valid window
            while unmatchedCount == 0:
                subStrLength = end - start + 1
                #we calculate the current length of valid substr
                if subStrLength < resultStrPosition[1]:
                    resultStrPosition = [start, subStrLength]
                #we increase start position to shrink window as long as we still have valid window
                #0 means under current window we have a perfect match for this character
                #means we should increase the unmatachedcount once we move away from it
                if s[start] in strMap:
                    if strMap[s[start]] == 0:
                        unmatchedCount += 1
                    strMap[s[start]] += 1
                start +=1
            #we move on till unmatchedCount is 0 which means we have satisfy substring
            end += 1
        if resultStrPosition[0] == -1:
            return ""
        return s[resultStrPosition[0]:resultStrPosition[0] + resultStrPosition[1]]

