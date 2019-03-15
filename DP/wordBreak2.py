https://leetcode.com/problems/word-break-ii/
#Similar approach as word break one, we store all possible cut ways in previous dp[i]
#complexity, cut or dont cut at each position, 2^n
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dpArray = [ [] for i in range(len(s) + 1)]
        #we treat length 0 prev str has a empty match
        dpArray[0] = [""]
        for i in range(1, len(dpArray)):
            #check all possible cut ways
            for j in range(0, i):
                if s[j:i] in wordDict and dpArray[j]:
                    for x in range(len(dpArray[j])):
                        newSubStr = dpArray[j][x] + s[j:i] + " "
                        dpArray[i].append(newSubStr)

        for x in range(len(dpArray[len(s)])):
            dpArray[len(s)][x] = dpArray[len(s)][x].rstrip()
        return dpArray[len(s)]