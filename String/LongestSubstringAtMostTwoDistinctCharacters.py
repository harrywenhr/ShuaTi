https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/


#sliding window, 2 pointers
for maximum, we increase the start index to shrink the window 
as long as its invalid to get a max valid window

if for minimum, we increase the start index to shrink the window 
as long as its valid to get a min valid window


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        #str map records number of matched characters in current window
        strMap = {}
        start = end = 0
        distinctCount = len(strMap)
        ressubStringPosition = [-1, 0]
        while end < len(s):
            #modify count
            #its a new distinct str
            if s[end] not in strMap or strMap[s[end]] == 0:
                strMap[s[end]] = 1
                distinctCount += 1
            else:
                strMap[s[end]] += 1
            #as long as we current window is invalid, we increase start index to shrink window
            while(distinctCount > 2):
                strMap[s[start]] -= 1
                if strMap[s[start]] == 0:
                    #once we move out the start index, current window will not contain this type of character, we decrease count
                    distinctCount -= 1
                start += 1
            #we have a valid window now, we update the result and move the right index
            newStrLength = end - start + 1
            if ressubStringPosition[0] == -1:
                ressubStringPosition = [start, newStrLength]
            else:
                if ressubStringPosition[1] < newStrLength:
                    ressubStringPosition = [start, newStrLength]
            end += 1
        if ressubStringPosition[0] == -1:
            return 0
        return ressubStringPosition[1]


