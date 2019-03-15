https://leetcode.com/problems/subsets-ii/
#if S[i] is same to S[i - 1], then it needn't to be added to all of the subset, 
# just add it to the last l subsets which are created by adding S[i - 1]
# we also use size to control where to add
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return self.iterative(nums)
    def iterative(self, nums):
        nums.sort()
        result = [[]]
        previousSubsetsCount = 1
        for index in range(len(nums)):
            startAdd = 0
            endAdd = len(result)
            #we have a dup, we only add to subsets that was added last time 
            #num[index - 1] was encounteded
            #which is start at previous result length
            if index > 0 and nums[index] == nums[index - 1]:
                startAdd = previousSubsetsCount
            for i in range(startAdd, endAdd):
                newSubset = list(result[i]) + [nums[index]]
                result.append(newSubset)
            previousSubsetsCount = endAdd
        return result

#practice
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        prevResultLength = len(result)
        for i in range(len(nums)):
            startToAdd = 0
            currentResultLength = len(result)
            if i > 0 and nums[i - 1] == nums[i]:
                #we only append to subsets has nums[i-1]
                startToAdd = prevResultLength
            for x in range(startToAdd, currentResultLength):
                newA = result[x] + [nums[i]]
                result.append(newA)
            prevResultLength = currentResultLength
        return result