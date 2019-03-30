https://leetcode.com/problems/house-robber-ii/



Suppose there are n houses, since house 0 and n - 1 are now neighbors, we cannot rob them together and thus the solution is now the maximum of

Rob houses 0 to n - 2;
Rob houses 1 to n - 1.


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n <= 3:
            return max(nums)

        #rob house from 0 to n - 2
        case1 = self.robHelper(nums, 0, n - 2)
        #rob house from 1 to n - 1
        case2 = self.robHelper(nums, 1, n - 1)
        return max(case1, case2)



    def robHelper(self, nums: List[int], start, end) -> int:
        prev1 = nums[start]
        prev2 = max(nums[start + 1], nums[start])
        for i in range(start + 2, end + 1):
            current = prev1 + nums[i]
            current = max(current, prev2)
            #print(current)
            prev1 = prev2
            prev2 = current
        return prev2


either we rob first house or we dont
case1, we rob first house

input starts from position 2 to last - 1

case2, we dont rob first house
inputs start from position 1 to last






    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n <= 3:
            return max(nums)
        dp = [0] * len(nums)
        #case1, we rob first house
        for i in range(2, n - 1):
            #rob current house
            case1 = nums[i] + dp[i - 2]
            #dont rob current house
            case2 = dp[i - 1]
            dp[i] = max(case1, case2)
        case1Max = dp[-2] + nums[0]
        dp = [0] * len(nums)
        #case2, we dont rob first house
        for i in range(1, n):
            case1 = nums[i] + (dp[i - 2] if i >= 2 else 0) 
            case2 = dp[i - 1]
            dp[i] = max(case1, case2)
        case2Max = dp[-1]
        return max(case1Max, case2Max)


