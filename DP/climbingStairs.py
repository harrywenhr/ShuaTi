https://leetcode.com/problems/climbing-stairs/

dp[n] = number of ways to n top
dp[n] = dp[n-1] + dp[n-2]
dp[0] = 1
class Solution:
    def climbStairs(self, n: int) -> int:
        dpArray = [0] * (n + 1)
        for i in range(len(dpArray)):
            if i == 0:
                dpArray[i] = 1
            else:
                dpArray[i] += dpArray[i - 1] + (dpArray[i - 2] if i >= 2 else 0)
        return dpArray[-1]