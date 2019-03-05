https://leetcode.com/problems/max-area-of-island/
#we loop through matrix, and start DFS on 1s, mark visited position to -1
class Solution:
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':
        if len(grid) == 0:
            return 0
        maxIsland = 0
        for row in range(0, len(grid)):
            for column in range(0, len(grid[0])):
                if grid[row][column] == 1:
                    currentIsland = self.dfs(grid, row, column)
                    maxIsland = max(maxIsland, currentIsland)
                    print("{0}, {1}, {2}".format(maxIsland, row, column))
        return maxIsland

    #we mark position as visited once we added that to stack
    def dfs(self, grid, row, column):
        currentArea = 1
        DFSStack = [[row, column]]
        grid[row][column] = -1      
        while DFSStack:
            print(DFSStack)
            currentPosition = DFSStack.pop()
            currentRow, currentColumn = currentPosition[0], currentPosition[1]
            #we visit neibors, only add 1s
            #make sure we within bounds
            for row, column in ((currentRow, currentColumn - 1), (currentRow, currentColumn + 1), (currentRow -1 , currentColumn), (currentRow +1 , currentColumn)):
                print("neibor {0} {1}".format(row, column))
                if (row >=0 and row < len(grid)) and (column >= 0 and column < len(grid[0])):
                    if grid[row][column] == 1:
                        #we visit valid position
                        currentArea += 1
                        #mark position as visited
                        grid[row][column] = -1
                        DFSStack.append([row, column])
        return currentArea

#practiced!
