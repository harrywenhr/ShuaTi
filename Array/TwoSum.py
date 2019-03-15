https://leetcode.com/problems/two-sum/submissions/
class Solution(object):
    def twoSum(self, nums, target):
        valueDic = {}
        for idx, num in enumerate(nums):
            if (target - num) in valueDic:
                return [valueDic[(target - num)], idx]
            #set destiny pair index
            valueDic[num] = idx
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#practiced