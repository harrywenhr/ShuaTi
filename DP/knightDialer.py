https://leetcode.com/problems/knight-dialer/
https://leetcode.com/problems/knight-dialer/discuss/189252/O(logN)
#number of walks (1-2-1-2-1) in adjacent matrix can by get by M**N
class Solution:
    def knightDialer(self, N):
        MOD = 10**9 + 7
        #index 0 can jump to 4,6
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]
        
        #from index 0-9, we the number of ways to dial (start, n) 
        #initially (start, 1) = 1
        #f(1, n) = f(6, n-1) + f(8, n-1)
        #f(1,2) = f(6,1) + f(8,1) = 2
        dp = [1] * 10
        for hops in range(N-1):
            #records current count of the different ways
            #here dp is the f(start, n-1)
            dp2 = [0] * 10
            for nodeIndex, count in enumerate(dp):
                for nextNodeIndex in moves[nodeIndex]:
                    dp2[nextNodeIndex] += count
                    dp2[nextNodeIndex] %= MOD
            dp = dp2
        return sum(dp) % MOD
class Solution:
    def knightDialer(self, N):
        MOD = 10**9 + 7
        #index 0 can jump to 4,6
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]

        #f(n - 1, nodeIndex) = number of ways start at nodexIndex with n-1 hops
        #like a recusively 1 = 2 + 2 = 2 + 2 + 2 + 2... so exponatial
        #f(n - 1, nodeIndex) = f(n - 2, nextP1) + f(n-2,nextP2)
        #f(0, nodeIndex) = 0
        #f(1, nodeIndex) = 1
        #we only need previous row here, so a row of length 10 can do it
        dpTable = [[0] * 10 for i in range(N + 1)]
        for i in range(1, N):
            for nodeIndex in range(10):
                if i == 1:
                    dpTable[i][nodeIndex] = 1
                else:
                    for nextNodeIndex in moves[nodeIndex]:
                        dpTable[i][nodeIndex] += dpTable[i - 1][nextNodeIndex]
        return sum(dpTable[-1]) % MOD

