https://leetcode.com/problems/next-greater-element-ii/submissions/

class Solution(object):
    def nextGreaterElements(self, nums):
        stack, res = [], [-1] * len(nums)
        #if we do it 2 time, its like all elements are listed 
        #to the right of array one more time
        for i in range(len(nums)) * 2:
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res
        