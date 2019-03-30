https://leetcode.com/problems/new-21-game/

dp[i] = p of getting i points
our answer is the sum of dp[K] + dp[K + 1]....dp[N]

dp[i] = dp[i - 1] + dp[i - 2] ..... dp[i - w] / w notice that we cannot add
dp[i - w] if i - w >= K 


dp[0] = 1 , 

prevWindowSum = 1 #start with 0 points, 100% p

dp[1] = prevWindowSum / W = 1 / W

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0 or N >= K + W:
            return 1.0
        if N < K:
            return 0.0
        dp = [0 for i in range(N + 1)]
        #we maintain a window sum of w dps
        windowSum = 1
        for i in range(N + 1):
            if i == 11:
                print(windowSum)
            if i == 0:
                dp[i] = 1.0
            else:
                dp[i] = windowSum / float(W)
                #once we reach K points, we need to stop, thus 
                #prevWindow cannot contain p where i >= K
                if i < K:
                    windowSum += dp[i]
                #we can now pop off a item from window sum
                if i - W >= 0:
                    windowSum -= dp[i - W]

        return sum(dp[K:])



dp(k,N) = p of ending at N or less points

dp(k,N) = (dp(k - 1, N - 1) + dp(k - 2, N - 2) .... +dp(k - W, N - W))/ W

#cant draw numbers, have some N left, same for k < 0
dp(0,N) = 1 
#need to continue draw, yet no N left, same for n < 0
dp(k,0) = 0
#can draw, have nothing left, no more than 0
dp(0,0) = 1

dp(1,10)

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [[0 for i in range(N + 1)] for j in range(K + 1)]
        for k in range(K + 1):
            for n in range(N + 1):
                if k == 0:
                    dp[k][n] = 1
                else:
                    currentP = 0
                    for x in range(1, W + 1):
                        caseP = 0
                        newK = k - x
                        newN = n - x
                        if newN >= 0:
                            caseP = dp[newK][newN] if newK >= 0 else 1
                        else:
                            caseP = 0
                        currentP += caseP
                    currentP = float(currentP) / float(W)
                    dp[k][n] = currentP
        return dp[K][N]




