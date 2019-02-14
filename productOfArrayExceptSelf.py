https://leetcode.com/problems/product-of-array-except-self/

Scan array one time to get production at current index ->Array P
Scan array second time from right to left
result = P[i - 1] * currentRightProduction
class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        if len(nums) <= 1:
            return nums
        resultA = [nums[0]]
        for i in range(1, len(nums)):
            newP = resultA[i - 1] * nums[i]
            resultA.append(newP)
        rightP = 1
        for i in range(len(nums) - 1, -1, -1):
            leftP = resultA[i - 1] if i > 0 else 1
            resultA[i] = leftP * rightP
            rightP *= nums[i]
        return resultA