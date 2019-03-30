https://leetcode.com/problems/house-robber/

dp[n] = max money at index n
dp[n] = max(dp[n - 2] + nums[n], dp[n-1])
dp[0] = nums[0]
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        prev1 = nums[0]
        prev2 = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            current = prev1 + nums[i]
            current = max(current, prev2)
            #print(current)
            prev1 = prev2
            prev2 = current
        return prev2