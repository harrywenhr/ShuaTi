https://leetcode.com/problems/minimum-falling-path-sum/

dp[i][j] = min sum end with element at i,j

dp[0][j] = A[0][j]

dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1]) + A[i][j]

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        dp = [[0 for i in range(len(A[0]))] for j in range(len(A))]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0:
                    dp[i][j] = A[i][j]
                else:
                    case1 = dp[i - 1][j]
                    case2 = dp[i - 1][j - 1] if j > 0 else sys.maxsize
                    case3 = dp[i - 1][j + 1] if j < len(dp[0]) - 1 else sys.maxsize
                    dp[i][j] = min(case1, case2, case3) + A[i][j]
        return min(dp[-1])