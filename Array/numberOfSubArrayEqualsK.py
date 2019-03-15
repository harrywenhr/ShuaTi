https://leetcode.com/problems/subarray-sum-equals-k/
Given an array of integers and an integer k, you need to find the total 
number of continuous subarrays whose sum equals to k.

#Key is Sum till j - Sum till i = K
#we use hashmap to stored number of occurence of each different sum
# if there has been a Sum till i = newSum - K, we have a answer and 
#we increase answer counnt
# We update the hashmap with occurennce of Sum
# Careful that if Sum till i = newSum - K = 0, we must store a 0 in hashmap
# for previous imagine elements before first one
# We add the result count first, then update the current sum count
class Solution:
    def subarraySum(self, nums: 'List[int]', k: 'int') -> 'int':
        if len(nums) < 1:
            return 0
        hashmap = {0:1}
        currentSum = 0
        resultCount = 0
        for number in nums:
            currentSum += number
            findSum = currentSum - k
            if findSum in hashmap:
                #we have a match
                resultCount += hashmap[findSum]
            if currentSum not in hashmap:
                hashmap[currentSum] = 1
            else:
                hashmap[currentSum] += 1
            

        return resultCount


#practice
class Solution:
    def subarraySum(self, nums: 'List[int]', k: 'int') -> 'int':
        if len(nums) == 0:
            return 0
        #number of ways sum to 0
        sumMap = {0:1}
        currentSum = 0
        result = 0
        for number in nums:
            currentSum += number
            lookSum = currentSum - k
            if lookSum in sumMap:
                result += sumMap[lookSum]
            if currentSum in sumMap:
                sumMap[currentSum] += 1
            else:
                sumMap[currentSum] = 1
        return result
