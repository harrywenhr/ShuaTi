https://leetcode.com/problems/knight-probability-in-chessboard/

dp(k, r, c) = (dp(k-1, r1, c1) + dp(k-1, r2, c2) ...... dp(k-1, r8, c8) ) / 8

r1,c1 = r - 1, c - 2
r2,c2 = r - 1, c + 2
r3,c3 = r - 2, c - 1
r4,c4 = r + 2, c + 1

dp(0,r,c) = 1 as long as r c are in board
dp(k,r,c) = 0 if r,c are not in board
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        #initially K = 0, everything is 1
        dpTablePrevs = [[1 for i in range(N)] for j in range(N)]
        for k in range(1, K + 1):
            dpTableCurrent = [[0 for i in range(N)] for j in range(N)]
            for i in range(N):
                for j in range(N):
                    currentP = 0
                    for move in self.nextMoves(i, j):
                        caseP = 0
                        if move[0] >= 0 and move[0] < N and move[1] >= 0 and move[1] < N:
                            caseP = dpTablePrevs[move[0]][move[1]]
                            #print("{0} {1} {2}".format(i, j, caseP))
                        currentP += caseP
                    resP = float(currentP) / 8.0
                    if k == K and i == r and j == c:
                        return resP
                    dpTableCurrent[i][j] = resP
            dpTablePrevs = dpTableCurrent
        return 1.0

    def nextMoves(self, r, c):
        nextM = []
        for newR,newC in ((r - 1, c - 2), (r - 1, c + 2), (r + 1, c - 2), (r + 1, c + 2), \
                          (r - 2, c - 1), (r - 2, c + 1), (r + 2, c - 1), (r + 2, c + 1)):
            nextM.append([newR, newC])
        return nextM

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp = {}
        return self.helper(N, r, c, K, dp)
    def helper(self, N,r, c, currentK, dp):
        #check if current point is valid
        if c < 0 or c >= N or r < 0 or r >= N:
            return 0
        #check if we can move or not
        if currentK == 0:
            return 1
        #get next state
        #check for memo
        currentTuple = (currentK, r, c)
        if currentTuple in dp:
            return dp[currentTuple]
        newP = 0
        for newR,newC in ((r - 1, c - 2), (r - 1, c + 2), (r + 1, c - 2), (r + 1, c + 2), \
                          (r - 2, c - 1), (r - 2, c + 1), (r + 2, c - 1), (r + 2, c + 1)):
            newP += self.helper(N, newR, newC, currentK - 1, dp)
        currentP = float(newP) / 8.0
        return currentP