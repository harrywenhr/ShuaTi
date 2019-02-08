# https://leetcode.com/problems/4sum/

# a + b + c + d = target

# for every element x in List
# new target = target - x
# find 
# a + b + c = newTarget  its a 3sum problem now


class Solution:
    def fourSum(self, nums: 'List[int]', target: 'int') -> 'List[List[int]]':
        #current pick element range, number of elements to pick
        #current target to look for
        #current picked elemets in result
        #current final answer list
        def findNSum(leftI, rightI, N, target, result, results):
            #termination conditions, base case in N=2, not enough elements to pick
            #Elements left are too big
            #Elements left are too small
            if N < 2 or (rightI - leftI + 1) < N or (nums[leftI] * N > target) or (nums[rightI] * N < target):
                return
            #base case
            if N == 2:
                while leftI < rightI:
                    s = nums[leftI] + nums[rightI]
                    if s == target:
                        results.append(result + [nums[leftI], nums[rightI]])
                        #we move left and right index to next different one
                        leftI += 1
                        rightI -= 1
                        while (leftI < rightI) and (nums[leftI] == nums[leftI - 1]):
                            leftI += 1
                        while (leftI < rightI) and (nums[rightI] == nums[rightI + 1]):
                            rightI -= 1                         
                    elif s > target:
                        # too big, we move rightI left
                        rightI -= 1
                    elif s < target:
                        # too small, we move leftI right
                        leftI += 1

            #we do our recusive here
            for i in range(leftI, rightI + 1):
                #we skip same elements as we have encountered them before
                #we pick one element, reset the target and continue our recusive run
                if i == leftI or nums[i] > nums[i - 1]:
                    #append returns value none
                    #result.append(nums[i])
                    #currentResult = result + [nums[i]]
                    findNSum(i + 1, rightI, N - 1, target - nums[i], result + [nums[i]], results)
        nums.sort()
        results = []
        findNSum(0, len(nums) - 1, 4, target, [], results)
        return results

