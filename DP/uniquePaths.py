https://leetcode.com/problems/unique-paths/

dp[n,n] = dp[n-1,n] + dp[n, n - 1]
dp[0,0] = 1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dpTable = [[0 for i in range(m)] for j in range(n)]
        if not dpTable:
            return 0
        for i in range(n):
            for j in range(m):
                if i == j == 0:
                    dpTable[i][j] = 1
                else:
                    case1 = dpTable[i - 1][j] if i > 0 else 0
                    case2 = dpTable[i][j - 1] if j > 0 else 0
                    dpTable[i][j] = case1 + case2
        return dpTable[-1][-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [1] * m
        if not prevRow:
            return 0        
        for i in range(1, n):
            currRow = []
            for j in range(m):
                case1 = prevRow[j]
                case2 = currRow[-1] if currRow else 0
                currRow.append(case1 + case2)
            prevRow = currRow
        return prevRow[-1]
