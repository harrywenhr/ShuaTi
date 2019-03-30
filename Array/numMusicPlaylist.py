https://leetcode.com/problems/number-of-music-playlists/
https://leetcode.com/problems/number-of-music-playlists/discuss/178415/C%2B%2BJavaPython-DP-Solution


Your music player contains N different songs and she wants to listen 
to L (not necessarily different) songs during your trip. 
 You create a playlist so that:

Every song is played at least once so we keep decreasing till we hit 1
A song can only be played again only if K other songs have been played
Return the number of possible playlists.


Let dp[i][j] be the number of playlists of length i that have exactly 
j unique songs. We want dp[L][N], and it seems likely we can develop 
a recurrence for dp.

#last song can be the first time we played
#Or we played that song before, be have k other songs in between
dp[L][N] = dp[L - 1][N - 1] * N + dp[L-1][N] * (N - K)
dp[n][n] = n!
and l must >= n > k
so base case is dp[l][n] where l == n, we do n!

class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        MOD = 10**9 + 7
        dpTable = [[0 for i in range(N + 1)] for j in range(L + 1)]
        dpTable[0][0] = 1
        for l in range(K + 1, L + 1):
            for n in range(K + 1, N + 1):
                if l == n:
                    dp[l][n] = math.factorial(n)
                else:
                    #we only need previous row information
                    dpTable[l][n] = dpTable[l - 1][n - 1] * n + dpTable[l - 1][n] * (n - K)
        return dpTable[L][N] % MOD



    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        MOD = 10**9 + 7
        res = 1
        currentUsed = 0

        for i in range(L):
            currentChoice = N - currentUsed
            #we cannot produce a single valid playlist
            if currentChoice == 0:
                return 0
            print(currentChoice)
            res *= currentChoice
            if currentUsed < K:
                currentUsed += 1
            else:
                if i < N:
                    #we have not used all song, we keep increasing the currentUsed
                    currentUsed += 1
        return res % MOD
