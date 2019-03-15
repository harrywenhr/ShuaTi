#https://leetcode.com/problems/search-in-rotated-sorted-array/


#Careful we need to check if we are still in rotated array or not !
#Careful for checking if start > end

# binary search
# 1. equal our target 
# check if we are still in rotate array
# if n[mid] >= n[start] -> we are on first ascending slope
    # if n[start] <=target <= n[mid] -> normal sorted array
    # else mid + 1 to end
# if n[mid] <= n[end] -> we are on second ascending slope
    # if n[mid] <= target <= n[end] -> normal sorted array
    # else start to mid - 1

#https://leetcode.windliang.cc/leetCode-33-Search-in-Rotated-Sorted-Array.html
#when we get a mid, either start mid is sorted or mid end is sorted
#we check if target is in sorted part, if so, go on, if not discard the sorted part



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            #consider equal as mid may land on beginning
            if nums[mid] >= nums[left]:
                #left part sorted
                if nums[left] <= target < nums[mid]:
                    #target in sorted part
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                #sorted on right
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1





class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        if len(nums) == 0:
            return -1
        return self.rotateSearch(nums, 0, len(nums) - 1, target)
    def rotateSearch(self, nums, start, end, target):
        if start > end:
            return -1
        print("rotateSearch {0} {1}".format(start, end))
        # we are not in rotated array!
        if nums[start] < nums[end]:
            return self.sortSearch(nums, start, end, target)
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[start]:
            if (nums[start] <= target) and (target <= nums[mid]):
                return self.sortSearch(nums, start, mid - 1, target)
            else:
                return self.rotateSearch(nums, mid + 1, end, target)
        if nums[mid] <= nums[end]:
            if (nums[mid] <= target) and (target <= nums[end]):
                return self.sortSearch(nums, mid + 1, end, target)
            else:
                return self.rotateSearch(nums, start, mid - 1, target)
        return -1



    def sortSearch(self, nums, start, end, target):
        print("sortSearch {0} {1}".format(start, end))
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
        return -1




#practice
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            #consider equal as mid may land on beginning
            if nums[mid] >= nums[left]:
                #left part sorted
                if nums[left] <= target < nums[mid]:
                    #target in sorted part
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                #sorted on right
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1        