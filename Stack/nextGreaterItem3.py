https://leetcode.com/problems/next-greater-element-iii/
Given a positive 32-bit integer n, you need to find the smallest 
32-bit integer which has exactly the same digits existing in the 
integer n and is greater in value than n. If no such positive 
32-bit integer exists, you need to return -1.

#same as next permutation
#we scan through array from right to left, find first one
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if len(str(n)) <= 1:
            return -1
        numberArray = list(map(int, str(n)))
        swapIndex1 = -1
        #print(numberArray)
        for i in range(len(numberArray) - 1, 0, -1):
            #print(i)
            if numberArray[i] > numberArray[i - 1]:
                swapIndex1 = i - 1
                break
        #we have a perfect descending array
        if swapIndex1 == -1:
            return -1
        swapIndex2 = swapIndex1 + 1
        #print(swapIndex1)
        while swapIndex2 < len(numberArray) and numberArray[swapIndex2] > numberArray[swapIndex1]:
            swapIndex2 += 1
        swapIndex2 -= 1
        numberArray[swapIndex1], numberArray[swapIndex2] = numberArray[swapIndex2], numberArray[swapIndex1]
        leftI = swapIndex1 + 1
        rightI = len(numberArray) - 1
        while leftI < rightI:
            numberArray[leftI], numberArray[rightI] = numberArray[rightI], numberArray[leftI]
            leftI += 1
            rightI -= 1
        strArray = list(map(str, numberArray))
        numberStr = "".join(strArray)
        return int(numberStr) if int(numberStr)<=((1<<31)-1) else -1



        