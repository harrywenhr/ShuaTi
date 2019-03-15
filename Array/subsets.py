https://leetcode.com/problems/subsets/

#for subset of previus one, append one at the end as new added subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #return self.subsetsHelper(nums, len(nums) - 1)
        return self.iterative(nums)
    def subsetsHelper(self, nums, index):
        if index < 0:
            return [[]]
        previousSets = self.subsetsHelper(nums, index - 1)
        newFormedSets = []
        for subset in previousSets:
            newSet = list(subset) + [nums[index]]
            newFormedSets.append(newSet)
        return newFormedSets + previousSets

    #for every previous subset, we add a copy to it and add a[i] to end 
    #of copy we get the previous subsets number, use that as our 
    #stopping point for adding new subsets
    def iterative(self, nums):
        result = [[]]
        for number in nums:
            previousSubsetsCount = len(result)
            for i in range(previousSubsetsCount):
                newSubset = list(result[i]) + [number]
                result.append(newSubset)
        return result

#praticed