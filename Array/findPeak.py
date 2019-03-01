https://leetcode.com/problems/find-peak-element/

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.


#Binary search, if mid is not peak, we go to the neibor with higher value





class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # nums.insert(0, -sys.maxsize)
        # nums.append(-sys.maxsize)
        # peakIndex = self.findPeakHelper(nums, 0, len(nums) - 1)
        # return peakIndex - 1
        return self.findPeakHelper2(nums)
    #we always go for the high neibor part for potentail peak
    def findPeakHelper2(self, nums):
        #there is always a peak
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            leftValue = nums[mid - 1] if mid > 0 else -sys.maxsize
            rightValue = nums[mid + 1] if mid < (len(nums) - 1) else -sys.maxsize
            if nums[mid] > leftValue and nums[mid] > rightValue:
                return mid
            #we go left as left is higher
            if leftValue > nums[mid]:
                right = mid
            else:
                #we go right, we do not include mid here it has be covered by first case
                left = mid + 1
        return left

    def findPeakHelper(self, nums, start, end):
        #base case, need at least 3 item for a peak
        if (end - start) <= 1:
            return -1
        midIndex = start + (end - start) // 2
        if nums[midIndex] > nums[midIndex - 1] and nums[midIndex] > nums[midIndex + 1]:
            return midIndex
        #mid is a potential peak, we go to the higher neibor part as its guarantee for a peak position
        if nums[midIndex] >= nums[start] and nums[midIndex] >= nums[end]:
            if nums[midIndex] < nums[midIndex + 1]:
                #we go right
                return self.findPeakHelper(nums, midIndex, end)
            if nums[midIndex - 1] > nums[midIndex]:
                #we go left
                return self.findPeakHelper(nums, start, midIndex)
        #mid is a bottom, there could be peak at both ways, we pick left
        if nums[midIndex] < nums[start] and nums[midIndex] < nums[end]:
            return self.findPeakHelper(nums, start, midIndex)
        #start is high, we go left to find a peak
        if nums[start] > nums[midIndex]:
            return self.findPeakHelper(nums, start, midIndex)
        if nums[end] > nums[midIndex]:
            return self.findPeakHelper(nums, midIndex, end)
