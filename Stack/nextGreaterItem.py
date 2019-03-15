https://leetcode.com/problems/next-greater-element-i/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreaterMap = {}
        stack = []
        for number in nums2:
            while stack and stack[-1] < number:
                prevNumber = stack.pop()
                nextGreaterMap[prevNumber] = number
            stack.append(number)
        while stack:
            nextGreaterMap[stack.pop()] = -1
        for i in range(len(nums1)):
            nums1[i] = nextGreaterMap[nums1[i]]
        return nums1