https://leetcode.com/problems/super-egg-drop/


dp[M][K]means that, given K eggs and M moves,
what is the maximum number of floor that we can check.


dp[M][0] = 0
dp[1][K] = 1
dp[0][K] = 0
dp[M][1] = M

dp[M][K] = case1 + case2 + 1
case1 = dp[M - 1][K - 1]
case2 = dp[M - 1][K]


O(KlogN) Time, O(NK) Space
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0 for i in range(K + 1)] for j in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, K + 1):
                #dp increases exponentially 
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + 1
            if dp[i][j] >= N:
                return i



















f(i,j) = i eggs with j floors, minimum moves in worst case
f(1,100) = 100
f(1,j) = j (j >= 0)
f(x,0) = 0

f(i, j) = 
case1 = f(i - 1, w - 1) + 1
case2 = f(i, j - w) + 1

f(i,j)=min{max{case1,case2}}|1<=w<=j}

for all i > j, f(i,j) = f(j,j) //no need for more eggs
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        K = N if K > N
        dp = [[0 for i in range(1, K + 1)] for j in range(N + 1)]
        for i in range(1, K + 1):
            for j in range(N + 1):
                if i == 1:
                    dp[i][j] = j
                else:
                    if j == 0:
                        dp[i][j] = 0
                    else:
                        currentMinMove = sys.maxsize
                        for w in range(1,j + 1):
                            #egg breaks at floor w
                            case1 = dp[i - 1][w - 1] + 1
                            #egg does not break at floor w
                            case2 = dp[i][j - w] + 1
                            currentMinMove = min(currentMinMove, max(case1, case2))
                        dp[i][j] = currentMinMove
        return dp[-1][-1]
