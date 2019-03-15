#https://leetcode.com/problems/next-permutation/

# we travel backwards from list until we hit a smaller one, we switch it
# with the next higher element (rightmost)
# and rearrange trailing ones ascending (reverse it since it still
# comply with descending)

class Solution:
    def nextPermutation(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        #looping backwards
        for i in range(len(nums) -1, 0, -1):
            if nums[i - 1] < nums[i]:
                #we found our switching number!, we now try to find the next bigger one
                j = i
                while (j < len(nums)) and (nums[j] > nums[i - 1]):
                    #we keep going
                    j += 1
                #we should switch j -1 and i - 1 element
                tmp = nums[i - 1]
                nums[i - 1] = nums[j - 1]
                nums[j - 1] = tmp
                #we now reverse the trailing part from i to end
                self.reverseArray(nums, i, len(nums) - 1)
                break
            elif i == 1:
                #we are at the start of the array, its entirely descending, we reverse it all
                self.reverseArray(nums, 0, len(nums) - 1)
    def reverseArray(self, nums, start, end):
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start += 1
            end -= 1

#practice

class Solution:
    def nextPermutation(self, nums: 'List[int]') -> 'None':
        if len(nums) <= 1:
            return
        for i in range(len(nums) - 1, 0, -1):
            #found the smaller one
            if nums[i] > nums[i - 1]:
                swapIndex1 = i - 1
                swapIndex2 = i
                while(swapIndex2 < len(nums) and nums[swapIndex2] > nums[swapIndex1]):
                    swapIndex2 += 1
                swapIndex2 -= 1
                nums[swapIndex1], nums[swapIndex2] = nums[swapIndex2], nums[swapIndex1]
                self.revert(nums, i, len(nums) - 1)
                return
        #we hit a desending array
        self.revert(nums, 0, len(nums) - 1)
    def revert(self, nums, start, end):
        while start < end:
            nums[start],nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

