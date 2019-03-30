https://leetcode.com/problems/3sum/
# 1. Sort all element of array
# 2. Run loop from i=0 to n-2.
#      Initialize two index variables l=i+1 and r=n-1
# 4. while (l < r) 
#      Check sum of arr[i], arr[l], arr[r] is
#      zero or not if sum is zero then print the
#      triplet and do l++ and r--.
#      if the number is the same as the number before, 
#.     we have used it as target already, continue.
#      we need to move the left and right pointers to the 
#.     next different numbers, so we do not get repeating result.

# 5. If sum is less than zero then l++
# 6. If sum is greater than zero then r--
# 7. If not exist in array then print not found.
#[-4,-1,-1,0,1,2]



class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        res = []
        if len(nums) < 3:
            return res
        nums.sort()
        # the target index is from 0 to len - 3, think this as a shifting window with length 3
        for i in range(len(nums) - 2):
            leftI = i + 1
            rightI = len(nums) - 1
            #we already dealed with current number before, we continue
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            if nums[i] > 0:
                #impossible now since all numbers are positive from this point
                break
            while leftI < rightI:
                total = nums[i] + nums[leftI] + nums[rightI]            
                if total == 0:
                    #we found our triple, we add to res
                    #print("whattt {0} {1} {2}".format(i, leftI, rightI))
                    res.append([nums[i], nums[leftI], nums[rightI]])
                    leftI += 1
                    rightI -= 1
                    #need to make sure new leftI number is different then old one
                    #same thing for right
                    while (nums[leftI] == nums[leftI - 1] and leftI < rightI):
                        leftI += 1
                    while (nums[rightI] == nums[rightI + 1] and leftI < rightI):
                        rightI -= 1
                elif total > 0:
                    #too large, we need to move rightI to left
                    rightI -= 1
                elif total < 0:
                    #too small, we move leftI to right
                    leftI += 1
            #we have checked all posibilities on current index i, we move on
        return res





class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i]
            if target > 0:
                break
            leftI = i + 1
            rightI = len(nums) - 1
            while leftI < rightI:
                if target + nums[leftI] + nums[rightI] == 0:
                    res.append([target, nums[leftI], nums[rightI]])
                    leftI += 1
                    rightI -= 1
                    while (nums[leftI - 1] == nums[leftI] and leftI < rightI):
                        leftI += 1
                    while (nums[rightI + 1] == nums[rightI] and leftI < rightI):
                        rightI -= 1
                elif target + nums[leftI] + nums[rightI] > 0:
                    rightI -= 1
                else:
                    leftI += 1
        return res