https://leetcode.com/problems/find-the-duplicate-number/


# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
# prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

# #we treat this list as a linked list, where Node.value = nums[i], Node.nextindex = num[i]
# since nums[i] is between 1 to n, our nums array has index 0 - n 
# and no num[i] can point to index 0, so nums[0] is not 0 and will point to somewhere in array
# and we will always hit circles because:
# there's a duplicate in array, if we go pass it, we will end up in circles
# if we dont go pass it, means we hit circles before, only chance is we hit at nums[i] = i, but 
# in order to get to i, we must hit a nums[i] before, which proves that we hit circles already
# nums[0] will never be part of circle
# we use slow, fast to find the cicle

#we return slowI becasue this is the start of the circle, and if we revisit slowI for the second time
#there must be at least 2 nums[i] == slowI
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slowI = fastI = 0
        while True:
            slowI = nums[slowI]
            fastI = nums[nums[fastI]]
            if slowI == fastI:
                #we found our circle, we put slowI to start and do 1 step at a time to find start of a loop
                break
        slowI = 0
        #print("start fastI {}".format(fastI))
        while slowI != fastI:
            slowI = nums[slowI]
            fastI = nums[fastI]
            # print(slowI)
            # print(fast)
        return slowI



#practice
#
class Solution:
    #nums[0] is a start of non circle part
    def findDuplicate(self, nums: List[int]) -> int:
        slowI = fastI = 0
        while True:
            slowI = nums[slowI]
            fastI = nums[nums[fastI]]
            if slowI == fastI:
                #we found the match
                break
        #we put slowI in begin again
        slowI = 0
        while True:
            slowI = nums[slowI]
            fastI = nums[fastI]
            if slowI == fastI
                break
        return slowI