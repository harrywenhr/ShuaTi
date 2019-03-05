https://leetcode.com/problems/jump-game-ii/


we mark the number of steps from position n to last element as jumps[i]
jumps[n - 1] = 0
need to find jumps[0]

we scan from right to left from n - 2, jumps[i] = min (jumps[i + 1] to jumps[i + a[i]]) + 1


#Greedy approach, for all elements within range of current element (curr, currEnd)
#curFarthest is the farthest point that all points in [curBegin, curEnd] can reach.
#Once the current point reaches curEnd, then trigger another jump (in order to go further we must use a step here)
# and set the new curEnd with curFarthest, then keep the above steps,



class Solution:
    def jump(self, nums: List[int]) -> int:
        start = end = farthest = step = 0
        #No need to check last element
        #We only do loop if we have more than 2 elements
        for i in range(len(nums) - 1):
            farthest = max(nums[i] + i, farthest)
            if i == end:
                end = farthest
                step += 1
                if farthest >= len(nums) - 1:
                    return step
        return step

    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        checkIndex = 0
        currentEnd = nums[checkIndex]
        maxReach = currentEnd
        step = 1
        while maxReach < len(nums) - 1:
            newCheckIndex = checkIndex + 1
            for i in range(checkIndex, currentEnd + 1):
                if (i + nums[i]) > maxReach:
                    maxReach = i + nums[i]
                    newCheckIndex = i
            checkIndex = newCheckIndex
            print(checkIndex)
            currentEnd = nums[checkIndex] + checkIndex
            step += 1

        return step

    def jump(self, nums: List[int]) -> int:
        jumps = [sys.maxsize] * len(nums)
        jumps[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            minStep = sys.maxsize
            if (i + nums[i]) >= (len(nums) - 1):
                jumps[i] = 1
            else:
                for j in range(i + 1, i + nums[i] + 1):
                    minStep = min(jumps[j], minStep)
                if minStep < sys.maxsize:
                    jumps[i] = minStep + 1
        return jumps[0]


#practice

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