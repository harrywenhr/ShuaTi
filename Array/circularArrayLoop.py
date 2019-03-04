# https://leetcode.com/problems/circular-array-loop/
# Just think it as finding a loop in Linkedlist, except that loops with only 1 element do not count. 
# Use a slow and fast pointer, slow pointer moves 1 step a time while fast pointer moves 2 steps a time. 
# If there is a loop (fast == slow), we return true, else if we meet element with different directions, 
# then the search fail, we set all elements along the way to 0. Because 0 is fail for sure so when later 
# search meet 0 we know the search will fail.
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums[i] > 0:
                nums[i] = nums[i] % len(nums)
            else:
                nums[i] = nums[i] % len(nums) - len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            slowIndex = fastIndex = i
            #we keep moveing as long as we dont hit 0, we dont change direction
            while(nums[slowIndex] != 0 and nums[fastIndex] != 0 and nums[slowIndex] * nums[i] > 0):
                #print(i)
                nextSlow = self.nextIndex(nums, slowIndex)
                if nums[nextSlow] * nums[i] < 0:
                    break
                nextFast = self.nextIndex(nums, fastIndex)
                if nums[nextFast] * nums[i] < 0:
                    break
                nextFast = self.nextIndex(nums, nextFast)
                # if nums[nextFast] * nums[i] < 0:
                #     break
                #print("nextSlow {}".format(nextSlow))
                #print("nextFast {}".format(nextFast))
                if nextSlow == nextFast:
                    #we met, but we may met due to looping on current index
                    if nextSlow == self.nextIndex(nums, nextSlow):
                        nums[nextSlow] = 0
                        break
                    return True
                slowIndex = nextSlow
                fastIndex = nextFast
            #print(nums)
            #we need to set every point to 0 before changing directions or looping at itself
            slowIndex = fastIndex = i
            nextI = self.nextIndex(nums, slowIndex)
            while(nums[slowIndex] * nums[nextI] > 0 and nums[slowIndex] != 0):
                nums[slowIndex] = 0
                slowIndex = nextI
                nextI = self.nextIndex(nums, slowIndex)
        return False
    #Careful for minues situations
    def nextIndex(self, nums, index):
        moveValueIndex = index + nums[index]
        residue = (moveValueIndex) % len(nums)
        newIndex = residue if residue >= 0 else (len(nums) + residue)
        return newIndex












class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if len(nums) <=1 :
            return False
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            slowI = fastI = i
            while True:
                slowI = self.nextIndex(nums, slowI)
                fastI = self.nextIndex(nums, self.nextIndex(nums, fastI))
                if fastI == -1:
                    #bad path
                    break
                if slowI == fastI:
                    if slowI == self.nextIndex(nums, slowI):
                        nums[slowI] = 0
                        break
                    return True
            slowI = i
            while(self.nextIndex(nums, slowI) >= 0):
                nextI = self.nextIndex(nums, slowI)
                nums[slowI] = 0
                slowI = nextI
        return False
                
    #we valid if we reverse direction here        
    def nextIndex(self, nums, index):
        if index == -1:
            return -1
        moveI = nums[index] % len(nums)
        nextI = (moveI + index) % len(nums)
        if nums[nextI] * nums[index] <= 0:
            return -1
        return nextI
