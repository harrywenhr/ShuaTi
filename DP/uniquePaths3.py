https://leetcode.com/problems/unique-paths-iii/

class Solution:
# for every position on grid, we have 4 choices
# Time Complexity: O(4^(R*C))
# worst case the valid path length will be R*C, then we can remove a stack
# Space Complexity O(R*C)


# Let dp(r, c, todo) be the number of paths starting from where we are (r, c),
#  and given that todo is the set of empty squares we've yet to walk on.

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        #at least start - end
        validPathLength = 2
        startPosition = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    validPathLength += 1
                if grid[i][j] == 1:
                    startPosition = (i, j)
        path = []
        results = []
        visited = set()
        self.helper(grid, startPosition[0], startPosition[1], path, visited, results, validPathLength)
        return len(results)

    def helper(self, grid, row, column, currentPath, visited, results, validPathLength):
        #print("{0} {1} {2} {3}".format(row, column, currentPath, visited))
        #within bounds
        if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]):
            return
        #not valid position
        if grid[row][column] == -1:
            return
        #if at the end
        if grid[row][column] == 2:
            if len(currentPath) + 1 == validPathLength:
                currentPath.append((row, column))
                results.append(list(currentPath))
                #we make sure when we return from current check point, the currentPath is same as entering
                del currentPath[-1]
                return
            #we reach end to soon, we return
            return
        #a valid point, we visit it now
        visited.add((row,column))
        #add to current path
        currentPath.append((row, column))
        #visit unvisted neighbors
        for neighborRow,neighborColumn in ((row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)):
            if (neighborRow, neighborColumn) not in visited:
                self.helper(grid, neighborRow, neighborColumn, currentPath, visited, results, validPathLength)
        #after we visit all neighbors, we unvisit current position for others to visit
        visited.remove((row, column))
        del currentPath[-1]