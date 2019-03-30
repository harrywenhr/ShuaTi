https://leetcode.com/problems/cherry-pickup/
https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-741-cherry-pickup/
https://leetcode.com/problems/cherry-pickup/discuss/165218/Java-O(N3)-DP-solution-w-specific-explanation
Key observation: (0,0) to (n-1, n-1) to (0, 0) is the same as (n-1,n-1) to (0,0) twice
same thing 2 people from start to end


Two people starting from (n-1, n-1) and go to (0, 0).
They move one step (left or up) at a time simultaneously. 
And pick up the cherry within the grid (if there is one).
if they ended up at the same grid with a cherry. Only one of them can 
pick up it.

x1,y1
x2,y2

x1 + y1 = x2 + y2
y2 = x1 + y1 - x2

Since two people move independently, there are 4 subproblems:
 (right, right), (right, down), (down, right), (down, down). Finally, we have:

dp(x1, y1, x2) = grid(x1,y1) + grid(x2,y2) + max(dp(x1, y1 - 1, x2 ), dp(x1, y1 - 1, x2 - 1), dp(x1 - 1, y1, x2), dp(x1 - 1, y1, x2 - 1))

O(N^3)

can optimize to O(N^2)

a series of matrixs along in z-axis, we only need the previousMatrix and currentMatrix

# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111


to get dp(1,1,1) we need access dp(1,0,1), dp(1,0,0), dp(0,1,1), dp(0,1,0)
if max result is negative, means no valid path we continue 
if dp has positive value, 

dp[0,0,0] = 1


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dpCube = [[[-sys.maxsize for x in range(n)] for y in range(n)] for z in range(n)]
        for x1 in range(n):
            for y1 in range(n):
                for x2 in range(n):
                    if x1 == y1 == x2 == 0:
                        dpCube[x1][y1][x2] = grid[x1][y1]
                    y2 = x1 + y1 - x2
                    if x1 < 0 or x1 >= n or x2 < 0 or x2 >= n:
                        continue
                    if y1 < 0 or y1 >= n or y2 < 0 or y2 >= n:
                        continue
                    else:
                        case1 = dpCube[x1][y1 - 1][x2] if y1 > 0 else -sys.maxsize
                        case2 = dpCube[x1 - 1][y1][x2]if x1 > 0 else -sys.maxsize
                        case3 = dpCube[x1 - 1][y1][x2 - 1] if x1 * x2 > 0 else -sys.maxsize
                        case4 = dpCube[x1][y1 - 1][x2 - 1] if y1 * x2 > 0 else -sys.maxsize
                        prevMax = max(case1, case2, case3, case4)
                        if prevMax < 0:
                            continue
                        if grid[x1][y1] < 0 or grid[x2][y2] < 0:
                            continue
                        dpCube[x1][y1][x2] = prevMax + grid[x1][y1]
                        #if we are at same cell we only count once cherry
                        if x1 != x2 or y1 != y2:
                            dpCube[x1][y1][x2] += grid[x2][y2]
        #print(dpCube)
        return dpCube[-1][-1][-1] if dpCube[-1][-1][-1] > 0 else 0



