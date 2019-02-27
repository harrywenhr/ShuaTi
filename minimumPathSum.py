https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



#classic dp
#minSum(m,n) = min(minSum(m-1, n) + matrix[m,n], minSum(m, n -1) + matrix[m,n]) 
#we build the dpTable from left to right and top to bottom, actually we can use the input matrix

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