https://leetcode.com/problems/bomb-enemy/

https://leetcode.com/problems/bomb-enemy/discuss/83383/Simple-DP-solution-in-Java

It's DP solution with complexity O (m*n).
We traversing along the row, the enemies killed between any w's is same,
 since we are shifting to next column, we need to compute for each column.
 Even for columns the enemies killed between w's is same.



class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m,n = len(grid), len(grid[0])
        #will be updated on each row scan
        #stores number of hits on this colomn between previous W and next W
        columnHits = [0 for i in range(n)]
        #stores number of hits on this row between previous W and next W
        currentRowHits = 0
        maxHits = 0

        def getRowHis(i,j):
            res = 0
            for x in range(j, n):
                if grid[i][x] == "E":
                    res += 1
                if grid[i][x] == 'W':
                    return res
            return res

        def getColomnHis(i,j):
            res = 0
            for x in range(i, m):
                if grid[x][j] == "E":
                    res += 1
                if grid[x][j] == 'W':
                    return res
            return res
        for i in range(m):
            for j in range(n):
                #we can now caculate the column hits
                if i == 0 or grid[i - 1][j] == "W":
                    #still O(MN) as we only visit those none W elements twice
                    columnHits[j] = getColomnHis(i,j)
                #get the row hits
                if j == 0 or grid[i][j - 1] == "W":
                    currentRowHits = getRowHis(i,j)
                #caculate the bomb hits
                if grid[i][j] == "0":
                    currentHits = currentRowHits + columnHits[j]
                    maxHits = max(currentHits, maxHits)
        return maxHits

