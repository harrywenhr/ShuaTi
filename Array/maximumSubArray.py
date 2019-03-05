https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.


class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        answer = nums[0]
        #We loop from left to right, if sum end in i -1 > 0
        #current maxSum = maxSum at i - 1 + nums[i]
        #else current maxSum = nums[i]
        for i in range(1, len(nums)):
            #here all previous i position has been updated with currentMaxSum
            if nums[i - 1] > 0:
                nums[i] = nums[i] + nums[i - 1]
            if nums[i] > answer:
                answer = nums[i]
        return answer


#practice
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return []
        maxSum = nums[0]
        for i in range(1, len(nums)):
            prevSumEnd = nums[i - 1]
            currentSum = max(prevSumEnd + nums[i], nums[i])
            maxSum = max(maxSum, currentSum)
            nums[i] = currentSum
        return maxSum