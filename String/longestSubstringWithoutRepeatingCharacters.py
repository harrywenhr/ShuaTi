https://leetcode.com/problems/longest-substring-without-repeating-characters/


#same sliding window
#to get a maximum, we move the start index as long as it a invalid window
#strMap records current number of chracter appearance for the window


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #record number of char occurance in current checking window
        strMap = {}
        start = end = 0
        #empty window has no repeating chracters
        #valid window, repeating chracter index
        windowStatus = [True, -1]
        resSize = 0
        while end < len(s):
            #we record current char
            strMap[s[end]] = strMap[s[end]] + 1 if s[end] in strMap else 1
            if strMap[s[end]] > 1:
                windowStatus = [False, end]
            #to get max, as long as current window is invalid, we increase left index
            while not windowStatus[0]:
                strMap[s[start]] -= 1
                if strMap[s[windowStatus[1]]] < 2:
                    windowStatus = [True, -1]
                start += 1
            #we have a valid window, we record size
            resSize = max(resSize, end - start + 1)
            end += 1
        return resSize