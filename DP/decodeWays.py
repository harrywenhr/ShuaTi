https://leetcode.com/problems/decode-ways/



dp(n) : number of ways for subStr length n
dp(n) = dp(n - 1) if last element 1 <= x <= 9 + dp(n - 2) if last 2 element <= 26

basecase
dp(0) = 1
dp(1) = 1
class Solution:
    def numDecodings(self, s: str) -> int:
        dpArray = [0 for i in range(len(s) + 1)]
        dpArray[0] = 1
        if not s:
            return 0
        for i in range(1, len(s) + 1):
            case1 = dpArray[i - 1] if int(s[i - 1]) > 0 else 0
            if i < 2:
                dpArray[i] = case1
            else:
                case2 = dpArray[i - 2] if (10 <= int(s[i - 2:i]) <= 26) else 0
                dpArray[i] = case1 + case2
        return dpArray[-1]