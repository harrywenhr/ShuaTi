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