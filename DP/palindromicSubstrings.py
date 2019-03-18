#https://leetcode.com/problems/palindromic-substrings/
class Solution:
    def countSubstrings(self, s: str) -> int:
    	p = self.getPalindromeArray(s)
    	finalSum = 0
    	for value in p:
    		finalSum += (value + 1) // 2
    	return finalSum
    def getPalindromeArray(self, s: str):
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

        return p

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