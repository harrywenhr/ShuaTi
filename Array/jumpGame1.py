https://leetcode.com/problems/jump-game/


Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

#we mark we can reach last index from index i Jumps[i], Jumps[n - 1] = 1
#from right to left, Jumps[i] can be determined on if i + a[i] landed at jumps array where we already marked as 1

#Jumps[0] is our answer

class Solution:

    #from right to left, we keep a index of a current left most good area
    #if a[i] + i >= leftMostGoodIndex
    #we update, else keep going
    #we check if leftMostGoodIndex == 0
    def canJump(self, nums: List[int]) -> bool:
        leftMostGoodIndex = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if (nums[i] + i) >= leftMostGoodIndex:
                leftMostGoodIndex = i
        if leftMostGoodIndex == 0:
            return True
        return False


    def canJump(self, nums: List[int]) -> bool:
        jumps = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                jumps[i] = 1
                continue
            canReach = nums[i] + i
            #we can reach the end
            if canReach >= (len(nums) - 1):
                jumps[i] = 1
            else:
                for j in range(i + 1, canReach + 1):
                    if jumps[j] == 1:
                        jumps[i] = 1
                        break
        return True if jumps[0] == 1 else False


#practice

class Solution:

    #from right to left, we keep a index of a current left most good area
    #good means we can reach end from here
    #if a[i] + i >= leftMostGoodIndex
    #we update, else keep going
    #we check if leftMostGoodIndex == 0
    def canJump(self, nums: List[int]) -> bool:
        leftMostGoodIndex = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= leftMostGoodIndex:
                leftMostGoodIndex = i
        if leftMostGoodIndex == 0:
            return True
        return False

