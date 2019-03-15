https://leetcode.com/problems/product-of-array-except-self/

Given an array nums of n integers where n > 1,  return an array output
such that output[i] is equal to the product of all the elements of nums 
except nums[i].
Note: Please solve it without division and in O(n).




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

#practice
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        output = [nums[0]]
        for i in range(1, len(nums)):
            newP = output[i - 1] * nums[i]
            output.append(newP)
        rightP = 1
        for i in range(len(nums) - 1, -1, -1):
            actualP = rightP * output[i - 1] if i >= 1 else rightP
            rightP *= nums[i]
            output[i] = actualP
        return output

