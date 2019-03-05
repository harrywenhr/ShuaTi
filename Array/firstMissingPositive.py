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
    #prefered
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



#practice

class Solution:
    #make a 1,2,3,4 ... filled array
    #the largest missing number is len(nums) + 1
    #we mark number - 1 position in array to negative represents we have this number  (if aready negtive, we got dups)
    #-4 will also remain its original value
    #we also need to mark the original nagative and larger then array number to some
    #invalid number, we use 1 in this case, so we first check if we miss 1 here
    #then we scan array return first non-agtive position + 1 as our missing number 
    #or len(nums) + 1
    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        missingOne = True
        for i in range(len(nums)):
            if nums[i] == 1:
                missingOne = False
            else:
                #no place for a 1,2,3,4 filled array
                if nums[i] < 1 or nums[i] > len(nums):
                    nums[i] = 1
        if missingOne:
            return 1
        for i in range(len(nums)):
            if nums[i] != 1:
                #we mark the filled position to negative, if its already nagtive we do nothing as current
                #one is a dup
                newP = abs(nums[i]) - 1
                if nums[newP] > 0:
                    nums[newP] = - nums[newP]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1
            
