https://leetcode.com/problems/move-zeroes/solution/
#two pointers, one at last non zero position
#one scan through, if its non zero, update first pointer as well
#if its zero, keep going until non zero, set last non zero position to current, set current to 0
#bump both
class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNoneZero = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[lastNoneZero] = nums[i]
                if i != lastNoneZero:
                    nums[i] = 0
                lastNoneZero += 1
