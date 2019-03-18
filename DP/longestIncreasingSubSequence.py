https://leetcode.com/problems/longest-increasing-subsequence/

https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

1. If A[i] is smallest among all end 
   candidates of active lists, we will start 
   new active list of length 1.

2. If A[i] is largest among all end candidates of 
  active lists, we will clone the largest active 
  list, and extend it by A[i].


3. If A[i] is in between, we will find a list with 
  largest end element that is smaller than A[i]. 
  Clone and extend this list by A[i]. We will discard all
  other lists of same length as that of this modified list.

A[0] = 0. Case 1. There are no active lists, create one.
0.


A[1] = 8. Case 2. Clone and extend.
0.
0, 8.

A[2] = 4. Case 3. Clone, extend and discard.
0.
0, 4.
0, 8. Discarded

#Need to ask if array has duplicates, and if sequence is stric increasing 
#keep a array which stores the end elememt of potential lists
#final length variable will be updated when new item is larger then all end element of potential lists
#actuall length of end elements array is the final length of longest increasing sub sequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        endElements = [nums[0]]
        resLength = 1
        for i in range(1, len(nums)):
            if nums[i] <= endElements[0]:
                #we insert current element as end of first active list (length 1), disgard existing length 1 end element
                #equvilent of relacing the end element of active list with length 1
                endElements[0] = nums[i]
            elif nums[i] > endElements[-1]:
                #clone existing one, append current element as the new end element
                endElements.append(nums[i])
            else:
                insertIndex = self.findInsertIndex(endElements, nums[i])
                #clone current insertIndex one list, append current at the end
                #equivilent of replacing insertIndex + 1 end element
                endElements[insertIndex + 1] = nums[i]
        return len(endElements)
    def findInsertIndex(self, endElements, targetNumber):
        left = 0
        right = len(endElements) - 1
        insertIndex = -1
        while left <= right:
            mid = left + (right - left) // 2
            if endElements[mid] == targetNumber:
                #stric increasing, we return previous one
                return mid - 1
            elif endElements[mid] < targetNumber:
                insertIndex = mid
                left = mid + 1
            else:
                right = mid - 1
        return insertIndex

