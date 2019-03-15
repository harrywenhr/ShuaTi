https://leetcode.com/problems/word-break/


# str pf length n
# dp(n) = for j from [0 to n - 1] if dp[j] and str[j:] in dict, set to true
# dp array has n + 1 positons for length [0, n]
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False
        dpArray = [False for i in range(len(s) + 1)]
        #if prev str is empty, we consider it exists in dicts
        dpArray[0] = True
        for i in range(1, len(dpArray)):
            #second part sub str start position is i - 1 since i means length here
            for j in range(0, i):
                #current cut position can full fill the condition, i is length here
                if dpArray[j] and s[j:i] in wordDict:
                    dpArray[i] = True
                    break
        return dpArray[len(s)]