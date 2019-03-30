https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

dp(i,j,k) = from [0,j], max sum and max sum indices for i maxSumOfThreeSubarrays

dp(i,j,k) = 
case1 we include last element into subarray
case2 we do not include

dp(i,j,k) = 
max (dp(i - 1, j - x, k) + arr[j - x + 1, j],
    dp(i, j - 1, k)
    )

dp(0,j,k) = 0
 
 j >= i * k - 1

O(N) to get sum at each index

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        numberOfSubarrays = 3
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        dp = [[[0,[]] for i in range(n)] for j in range(numberOfSubarrays + 1)]
        for i in range(1, numberOfSubarrays + 1):
            startJIndex = i * k - 1
            for j in range(startJIndex, n):
                case1 = dp[i - 1][j - k][0] + nums[j] - nums[j - k] if j >= k else nums[j]
                case2 = dp[i][j - 1][0]
                newIndices = []
                if case1 > case2:
                    prevIndices = dp[i - 1][j - k][1] if j >= k else []
                    newIndices = prevIndices + [j - k + 1]
                else:
                    newIndices = dp[i][j - 1][1]
                dp[i][j] = [max(case1, case2), newIndices]
        #print(dp)
        return dp[-1][-1][1]




