https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find the contiguous subarray within an
 array (containing at least one number) which has the largest product.

# we store the min and max value at value ending at position i

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        #we use number it self at first index for min and max
        previousMin = previousMax = nums[0]
        result = nums[0]
        #we only need to store previousMin and previousMax
        for i in range(1, len(nums)):
            currentMax = - sys.maxsize
            #when we product a negative number, we get the min by max*current, max by min*current
            if nums[i] < 0:
                currentMin = min(nums[i], previousMax * nums[i])
                currentMax = max(nums[i], previousMin * nums[i])
            else:
                currentMin = min(nums[i], previousMin * nums[i])
                currentMax = max(nums[i], previousMax * nums[i])
            result = max(result, currentMax)
            previousMin = currentMin
            previousMax = currentMax
        return result

#practice
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentMin = currentMax = previousMin = previousMax = nums[0]
        finalMax = currentMax
        for i in range(1, len(nums)):
            if nums[i] < 0:
                currentMin = min(nums[i], nums[i] * previousMax)
                currentMax = max(nums[i], nums[i] * previousMin)
            else:
                currentMin = min(nums[i], nums[i] * previousMin)
                currentMax = max(nums[i], nums[i] * previousMax)
            finalMax = max(finalMax, currentMax)
            previousMax = currentMax
            previousMin = currentMin
        return finalMax

