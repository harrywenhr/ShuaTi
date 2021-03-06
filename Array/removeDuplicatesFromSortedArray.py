https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array nums, remove the duplicates in-place such
 that each element appear only once and return the new length.

Do not allocate extra space for another array,
 you must do this by modifying the input array in-place with O(1) extra memory.



Keep 2 index, one checking index, one returnIndex
switch element only if checking index is different then return index
bump both index
class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums) < 2:
            return len(nums)
        checkingI = 1
        returnI = 0
        while checkingI < len(nums):
            #we have duplicates with current returnI, we move on
            while (checkingI < len(nums)) and (nums[checkingI] == nums[returnI]):
                checkingI += 1
            if checkingI == len(nums):
                #we have checked all numbers
                break
            #we are at checkingI number is different then current returnI num
            #we bumpe returnI and set it to current checkingI number
            returnI += 1
            nums[returnI] = nums[checkingI]
            #we move checkingI forward
            checkingI += 1
        return returnI + 1

#practiced
