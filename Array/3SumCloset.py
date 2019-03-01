
Same as 3Sum, we use a index i from 0 to n - 3, a left index and right index for find the 
closet sum to target, keep updated the current closest

class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        nums.sort()
        bestDistance = None
        bestSum = target
        for i in range(len(nums) - 2):
            leftI = i + 1
            rightI = len(nums) -1
            #we already checked the same number before, we move on
            if i > 0 and nums[i] == nums[i -1]:
                continue
            while leftI < rightI:
                total = nums[i] + nums[leftI] + nums[rightI]
                distance = abs(total - target)

                #we have a better result or we dont have result yet, update it
                if not bestDistance or distance < bestDistance:
                    bestDistance = distance
                    bestSum = total
                #we are at best, we return immediately
                if bestDistance == 0:
                    return total
                #we are too big, we should go small, move rightI to left
                if total - target > 0:
                    rightI -= 1
                #we are too small, we should go big, move leftI to right
                elif total - target < 0:
                    leftI += 1
        print("current distance {}".format(bestDistance))
        return bestSum





