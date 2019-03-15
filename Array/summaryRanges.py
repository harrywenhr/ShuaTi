https://leetcode.com/problems/summary-ranges/
Given a sorted integer array without duplicates, 
return the summary of its ranges.

#similar to find longest consective sequence, 
#this time we save the sequence while couting the lenght

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        setNums = set(nums)
        result = []
        for number in nums:
            #we found a starting element, we go ahead iterate through
            if (number - 1) not in setNums:
                resStr = str(number)
                startNumber = number + 1
                while startNumber in setNums:
                    startNumber += 1
                if startNumber - number > 1:
                    resStr += "->{}".format(startNumber - 1)
                result.append(resStr)
        return result

#practiced