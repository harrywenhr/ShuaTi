https://leetcode.com/problems/move-zeroes/
#two pointers, one at last non zero position
#one scan through, if its non zero, update first pointer as well
#if its zero, keep going until non zero, set last non zero 
#position to current, set current to 0
#bump both


# All elements before the slow pointer (lastNonZeroFoundAt) are non-zeroes.

# All elements between the current and slow pointer are zeroes.
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

#practice 

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        beforeThisAllNoneZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[beforeThisAllNoneZero] = nums[i]
                if i != beforeThisAllNoneZero:
                    nums[i] = 0
                beforeThisAllNoneZero += 1
