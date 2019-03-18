https://leetcode.com/problems/split-array-largest-sum/
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
 Write an algorithm to minimize the largest sum among these m subarrays.



given m bags with capacity X, we can use greedy method to check if we can put array items into
those bags
if current item will exceed the current bag, we put it into the next bag
O(n)

then for array, the smallerest max sum is the largest element in array, 
the largest max sum is the sum of array, we need to find the smallest capacity such that 
we can put those elements into m bags



class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        #binary search
        leftCapacity = max(nums)
        rightCapacity = sum(nums)
        leftCapacity = rightCapacity // m
        resultSum = 0
        while leftCapacity <= rightCapacity:
            midCapacity = leftCapacity + (rightCapacity - leftCapacity) // 2
            if self.canPutIntoBags(nums, m, midCapacity):
                #capacity is good, we keep going small to test the limit
                rightCapacity = midCapacity - 1
                resultSum = midCapacity
            else:
                #capacity is not good, we shoud increase
                leftCapacity = midCapacity + 1
        return resultSum

    def canPutIntoBags(self, nums, m, capacity):
        #greedy method
        bagNumber = 1
        currentBagWeight = 0
        for number in nums:
            if number > capacity:
                return False
            currentBagWeight += number
            #we need to put current item to next bag
            if currentBagWeight > capacity:
                bagNumber += 1
                currentBagWeight = number
            if bagNumber > m:
                #we exceed the bag count
                return False
        return True














#we cut array m - 1 times
here sub problem cutindex is increase compared to l, not good for bottom up
result(m - 1, l, r) = min(result(m - 2, cutIndex, r), sum[l to cutIndex]) for every cutIndex

result(1, l, r) = min(sum[l to cutindex], sum[cutindex to right]) for every possible cutIndex
to get result(2,l,r)





we cut at every possible position, cut to right is a sum, left to cut is from previous sub problem
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        sumArray= [nums[0]]
        for i in range(1, n):
            currentSum = sumArray[-1] + nums[i]
            sumArray.append(currentSum)
        if m == 1:
            return sumArray[-1]
        dpTable = [[sys.maxsize for i in range(n)] for j in range(m)]
        for cutTime in range(1, m):
            for cuttingAreaEnd in range(cutTime, n):
                for cutIndex in range(0, cuttingAreaEnd):
                    if cutTime == 1:
                        leftSum = sumArray[cutIndex]
                        rightSum = sumArray[cuttingAreaEnd] - sumArray[cutIndex]
                        # if cuttingAreaEnd == 1:
                        #     print("{} {}".format(leftSum, rightSum))
                        candidateSum = max(leftSum, rightSum)
                        dpTable[cutTime][cuttingAreaEnd] = min(candidateSum, dpTable[cutTime][cuttingAreaEnd])
                    else:
                        prevMinSum = dpTable[cutTime - 1][cutIndex]
                        rightSum = sumArray[cuttingAreaEnd] - sumArray[cutIndex]
                        candidateSum = max(prevMinSum, rightSum)
                        dpTable[cutTime][cuttingAreaEnd] = min(candidateSum, dpTable[cutTime][cuttingAreaEnd])
        return dpTable[m - 1][n - 1]