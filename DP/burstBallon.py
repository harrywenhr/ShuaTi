https://leetcode.com/problems/burst-balloons/
https://leetcode.com/problems/burst-balloons/discuss/76263/My-readable-Python-~500ms-accepted-solution-with-explanation


append 1 before and 1 after

I focus on the region (l,r), and assign m as the last balloon to be burst 
in this region. I need to calculate:
m cannot be l or r, means k >= 3

k = 2
k = 1 all 0 as theres no middle ballon to burst


max coins after the balloons in region (l,m) are burst, l, m not burst

max coins after the balloons in region (m,r) are burst, m, r not burst

nums[l]*nums[m]*nums[r]

*1 3,4,5 *1

60 + 15 + 5


k = 3
1,3,4 = 0 + 12 + 0
3,4,5 = 0 + 60 + 0
4,5,1 = 0 + 20 + 0

k = 4 

1,3,4,5 = max(0 + 15 + 3,4,5 = 75, 1,3,4 + 20 + 0 = 32) = 75

3,4,5,1 = max(0 + 12 + 4,5,1 = 32, 3,4,5 + 15 + 0 = 75) = 75

k = 5

1,3,4,5,1 = max(0 + 3 + 75, 12 + 4 + 20, 75 + 5 + 0) = 80


k from 3 to array + 2

dp[l][r] is the max coin in region (l,r) (l and r ballon not burst)


#remove 0s

1* 3 4 5 *1

1 3 4 = 0 + 12 + 0 = 12 dp[0,2]
3 4 5 = 0 + 60 + 0 = 60  dp[1,3]
4 5 1 = 0 + 20 + 0 = 20  dp[2,4]



class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+[n for n in nums if n!=0]+[1]
        n = len(nums)
        #careful for object reference!
        dpTable = [[0 for i in range(n)] for j in range(n)]
        #our region from 3 to n
        for k in range(3, n + 1):
            #last rightIndex is n - k + k - 1 = n - 1
            for leftI in range(0, n - k + 1):
                rightI = leftI + k - 1
                for midI in range(leftI + 1, rightI):
                    #valid middle index not equal to left and right
                    leftPortion = dpTable[leftI][midI]
                    rightPortion = dpTable[midI][rightI]
                    currentCoin = nums[midI] * nums[leftI] * nums[rightI]
                    currentRegion = leftPortion + rightPortion + currentCoin
                    dpTable[leftI][rightI] = max(dpTable[leftI][rightI], currentRegion)

        return dpTable[0][-1]




        