https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from 
top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



#classic dp
#minSum(m,n) = min(minSum(m-1, n) + matrix[m,n], minSum(m, n -1) + matrix[m,n]) 
#we build the dpTable from left to right and top to bottom, 
#actually we can use the input matrix to stored previous value

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                pathSum1 = grid[row - 1][column] if row > 0 else sys.maxsize
                pathSum2 = grid[row][column - 1] if column > 0 else sys.maxsize
                #watch out that we do not change first element value
                if row > 0 or column > 0:
                    grid[row][column] = min(pathSum1, pathSum2) + grid[row][column]
        return grid[len(grid) - 1][len(grid[0]) - 1]

#practice

class Solution:
    #pathS[m - 1][n - 1] = min(pathS[m - 2][n-1] + a[m-1][n-1], other direction)
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                path1 = grid[i - 1][j] if i >= 1 else sys.maxsize
                path2 = grid[i][j - 1] if j >= 1 else sys.maxsize
                grid[i][j] = min(path1, path2) + grid[i][j]
        return grid[-1][-1]

