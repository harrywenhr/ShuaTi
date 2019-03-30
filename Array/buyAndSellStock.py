https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        currentLow = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > currentLow:
                maxProfit = max(maxProfit, prices[i] - currentLow)
            else:
                currentLow = prices[i]
        return maxProfit



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        if len(prices) == 0:
            return 0
        lowerP = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < lowerP:
                lowerP = prices[i]
            else:
                currentP = prices[i] - lowerP
                maxP = max(currentP, maxP)
        return maxP


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        if len(prices) <= 1:
            return 0
        for i in range(1, len(prices)):
            gain = prices[i] - prices[i - 1]
            if gain > 0:
                maxP += gain
        return maxP



https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#as many transaction as you like

#we calculate profit as long as we are ascending up
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        maxProfit = 0
        for i in range(1, len(prices)):
            #we climb up, we add the profit
            if prices[i] > prices[i - 1]:
                maxProfit += prices[i] - prices[i - 1]
        return maxProfit

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
#at most 2 transaction

DP[i][j] represents the max profit until day j with at most i transactions,

if no transaction on day j, then no transaction subtracted from i, 
DP[i][j] = DP[i][j - 1](which is also the initialization)
if transaction happens on day j, then one transaction is subtracted 
from i, let's denote the day to buy as k,
DP[i][j] = prices[j] - prices[k] + DP[i - 1][k - 1](k = 0: j -1)
#either we do transaction at day j or we dont
then DP[i][j] = max(DP[i][j - 1], prices[j] - prices[k] + DP[i - 1][k - 1](k = 0: j - 1))
if(i == 0 || j == 0) DP[i][j] = 0;


Time complexity of above solution is O(kn) and space complexity is O(nk). Space complexity can further be reduced to O(n)
 as we uses the result from last transaction. But to make the article easily readable, we have used O(kn) space.


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        maxTransaction = k
        #careful for initialization, reuse array objects
        dpTable = [[0 for i in range(len(prices))] for j in range(maxTransaction + 1)]
        #print(dpTable)
        #number of transactins
        for i in range(1, maxTransaction + 1):
            #we use this to save max(dpTable[i - 1][x - 1] - prices[x])
            #as for a constant i, this value is only depended on x, which is from 0 to j - 1
            #we record the current max as x increases
            prevMax = -sys.maxsize
            #days
            for j in range(1, len(prices)):
                #we dont do transactin on day j
                profit1 = dpTable[i][j - 1]
                #we do one transaction with day x and day j
                profit2 = 0
                #this information can be optimized as get max(dpTable[i - 1][x - 1] - prices[x]) for x 0 to j - 1
                # for x in range(0, j):
                #     profit2 = max(prices[j] - prices[x] + (dpTable[i - 1][x - 1] if x > 0 else 0), profit2)

                #x - 1 = j - 1 - 1 = j - 2
                currentPrev = dpTable[i - 1][j - 2] if j >=2 else 0
                prevMax = max(prevMax,currentPrev - prices[j - 1])
                profit2 = prices[j] + prevMax

                dpTable[i][j] = max(profit1, profit2)
        #print(dpTable)
        return dpTable[maxTransaction][len(prices) - 1]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = 2
        if len(prices) <=1 :
            return 0
        dp = [[0 for i in range(len(prices))] for j in range(k + 1)]
        for i in range(len(dp)):
            #we mark max dp[i - 1][x - 1] - prices[x] from 0 till j - 1 as prevMax
            #so when new j comes, we compare current dp[i - 1][j - 2] - prices[j - 1] with prevMaX
            prevMax = -sys.maxsize
            for j in range(len(prices)):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    continue
                currentPrev = dp[i - 1][j - 2] if  j >= 2 else 0
                prevMax = max(prevMax, currentPrev - prices[j - 1])
                profit1 = dp[i][j - 1]
                profit2 = 0
                profit2 = prices[j] + prevMax
                # for x in range(0, j):
                #     profit2 = max(profit2, dp[i - 1][x - 1] + prices[j] - prices[x])
                dp[i][j] = max(profit1, profit2)
        return dp[k][-1]       