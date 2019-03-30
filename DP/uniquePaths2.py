https://leetcode.com/problems/unique-paths-ii/
dp[n,n] = dp[n-1,n] + dp[n, n - 1] if current grid is not obstacle else 0
dp[0,0] = 1
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        dpTable = [[0 for i in range(m)] for j in range(n)]
        if not dpTable:
            return 0
        for i in range(n):
            for j in range(m):
                if i == j == 0:
                    if obstacleGrid[i][j] != 1:
                        dpTable[i][j] = 1
                else:
                    case1 = dpTable[i - 1][j] if i > 0 else 0
                    case2 = dpTable[i][j - 1] if j > 0 else 0
                    dpTable[i][j] = case1 + case2
                    if obstacleGrid[i][j] == 1:
                        dpTable[i][j] = 0
        return dpTable[-1][-1]