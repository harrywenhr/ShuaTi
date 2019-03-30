https://leetcode.com/problems/perfect-squares/
same as coin change problem
https://leetcode.com/problems/coin-change/solution/
here we need to get a list of possible coins first



or BFS
https://leetcode.com/problems/perfect-squares/discuss/71475/Short-Python-solution-using-BFS
least number of coins = shortest path

from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        i = 1
        coinList = []
        while i**2 < n:
            coinList.append(i**2)
            i += 1
        if i**2 == n:
            return 1
        #save current level
        myQ = deque([[n, 0]])
        #important! we do not add visited value to our neibors
        visited = [False]*(n+1)
        while myQ:
            currentItem = myQ.popleft()
            currentSum = currentItem[0]
            currentLevel = currentItem[1]
            #we were able to make change for the coin
            if currentSum == 0:
                return currentItem[1]
            #visit current value
            visited[currentSum] = True
            for coin in coinList:
                if currentSum >= coin and not visited[currentSum - coin]:
                    myQ.append([currentSum - coin, currentLevel + 1])
        return -1

then F(n) as least number of ways to make coin to n
F(n) = min(F(n - c) + 1) for every c domination
let F(0) = 1 
F(negative) means we cant make change 
    def numSquares(self, n: int) -> int:
        i = 1
        coinList = []
        while i**2 < n:
            coinList.append(i**2)
            i += 1
        if i**2 == n:
            return 1
        dpArray = [sys.maxsize] * (n + 1)
        dpArray[0] = 1
        for totaNumber in range(1, n + 1):
            currentLeast = sys.maxsize
            for coinValue in coinList:
                currentLeast = min(currentLeast, dpArray[i - coinValue])
                if totaNumber < coinValue:
                    break
            if currentLeast < sys.maxsize:
                dpArray[totaNumber] = currentLeast + 1
        return dpArray[-1]
