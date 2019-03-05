
#Greedy approach, for all elements within range of current element (curr, currEnd)
#curFarthest is the farthest point that all points in [curBegin, curEnd] can reach.
#Once the current point reaches curEnd, then trigger another jump (in order to go further we must use a step here)
# and set the new curEnd with curFarthest, then keep the above steps,
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        currentIndex = 0
        currentReachableEnd = nums[0]
        minStep = 1
        nextReachableEnd = -1
        #no need check last element
        for i in range(len(nums) - 1):
            if currentReachableEnd >= (len(nums) - 1):
                #we can reach end now
                return minStep
            nextReachableEnd = max(nextReachableEnd, nums[i] + i)
            #we scaned everything in current reachable, we move on to next far point
            #we use a step here
            if i == currentReachableEnd:
                currentReachableEnd = nextReachableEnd
                minStep += 1
        if currentReachableEnd >= (len(nums) - 1):
            return minStep
        return -1


