https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.




#we use a set, put all numbers in
#for every number, we try to look for number - 1, if its not in set
#current number is a starting point of a sequence, we then continue the sequence to get the length
# each sequence will be count the lengh only once
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        result = 0
        for number in nums:
            #its a starting number for sequence, we count the length
            if (number - 1) not in numsSet:
                currentLength = 1
                startNumber = number
                #print(number)
                #print("aaa")
                while (startNumber + 1) in numsSet:
                    currentLength += 1
                    startNumber += 1
                #print(currentLength)
                result = max(result, currentLength)
        return result


#practice

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberSet = set()
        for n in nums:
            numberSet.add(n)
        maxL = 0
        for n in nums:
            if (n - 1) not in numberSet:
                startN = n
                sequenceL = 1
                while (startN + 1) in numberSet:
                    sequenceL += 1
                    startN += 1
                maxL = max(maxL, sequenceL)
        return maxL


        

