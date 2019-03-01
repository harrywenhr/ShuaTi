https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

#we use binary search, when search for first position, if equal, we go left
#we search last position, if equal, we go right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        startPosition = self.searchHelper(nums, target, 0, len(nums) - 1, True)
        endPosition = self.searchHelper(nums, target, 0, len(nums) - 1, False)
        return [startPosition, endPosition]
    def searchHelper(self, nums, target, start, end, isFirst):
        
        #base case
        if start > end:
            return -1
        #round to lower bound   
        midIndex = start + (end - start) // 2
        if nums[midIndex] == target:
            if isFirst:
                #we are search for first position, we go left if we can find anything left
                possibleLeft = self.searchHelper(nums, target, start, midIndex - 1, isFirst)
                return possibleLeft if possibleLeft >= 0 else midIndex
            possibleRight = self.searchHelper(nums, target, midIndex + 1, end, isFirst)
            return possibleRight if possibleRight >= 0 else midIndex
        elif nums[midIndex] < target:
            return self.searchHelper(nums, target, midIndex + 1, end, isFirst)
        else:
            return self.searchHelper(nums, target, start, midIndex - 1, isFirst)