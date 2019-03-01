#https://leetcode.com/problems/first-missing-positive/
we scan through array, we use array it self to arrange 1,2,3,4,5.....
if number <= 0 we set to 0
if number > len(nums) we set to 0
if number == index + 1, we set to "X"
if number > 0 and number < len(nums), we set nums[number - 1] = number 
and set original number follow the same rule

once done we scan array one more time to find first 0, if not, return one
more element after array




we check if missing positive is 1 !!!!!
if not, we scan array once set every number <= 0 and > len(nums) to 1
we scan array second time, if number > 1, set number - 1 position to negative
careful if we face duplicates

we scan array last time from second position, since we know we have 1 in array
return first non negative position + 1 or len(nums) + 1

class Solution:
    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        if len(nums) == 0:
            return 1
        hasOne = False
        for i in range(0, len(nums)):
            if nums[i] == 1:
                hasOne = True
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1
        if not hasOne:
            return 1
        for i in range(0, len(nums)):
            if abs(nums[i]) == 1:
                continue
            actualV = abs(nums[i])
            if nums[actualV - 1] > 0:
                nums[actualV - 1] = - nums[actualV - 1]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1


    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        if len(nums) == 0:
            return 1
        for i in range(0, len(nums)):
            currentValue = nums[i]
            if currentValue <= 0:
                nums[i] = 0
            elif currentValue > len(nums):
                nums[i] = 0
            elif currentValue == (i + 1):
                continue
            else:
                nums[i] = 0
                self.updateNumbers(nums, currentValue - 1, currentValue)
        #print(nums)
        for i in range(0, len(nums)):
            if nums[i] == 0:
                return i + 1
        return len(nums) + 1
    def updateNumbers(self, nums, index, updateValue):
        #print("updateNumbers {0} {1}".format(index, updateValue))
        currentValue = nums[index]
        if currentValue <= 0 or currentValue > len(nums):
            nums[index] = updateValue
        else:
            if currentValue == (index + 1):
                return
            nums[index] = updateValue
            self.updateNumbers(nums, currentValue - 1, currentValue)
            
