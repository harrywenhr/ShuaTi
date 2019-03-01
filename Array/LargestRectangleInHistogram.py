
https://leetcode.com/problems/largest-rectangle-in-histogram/
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.



For every bar ‘x’, we calculate the area with ‘x’ as the smallest bar in the rectangle
We need to know index of the first smaller (smaller than ‘x’) bar on left of ‘x’ and index of first smaller bar on right of ‘x’.
Use stack

ascending stack (if equal we just keep adding)
when a item x is poped, the first smaller index on left is its previous item on stack, the first small index on right is current index

area = currentItemHeight * (rightIndex - leftIndex - 1)


class Solution:
    def largestRectangleArea(self, heights: 'List[int]') -> 'int':
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]
        #we store index here
        heightStack = []
        maxArea = -1
        for i in range(0, len(heights)):
            if len(heightStack) == 0 or heights[i] >= heights[heightStack[-1]]:
                heightStack.append(i)
            else:
                while(len(heightStack) > 0 and heights[i] < heights[heightStack[-1]]):
                    #we found the smaller right index for current item on stack
                    #we calculate the result
                    currentItemHeight = heights[heightStack[-1]]
                    heightStack.pop()
                    #if we are at leftmost item, the smaller index would be one position left
                    leftIndex = heightStack[-1] if len(heightStack) > 0 else -1
                    area = currentItemHeight * (i - leftIndex - 1)
                    maxArea = max(area, maxArea)
                heightStack.append(i)
        #here the small right index would always be len(heights)
        while len(heightStack) > 0:
            currentItemHeight = heights[heightStack[-1]]
            rightIndex = len(heights)
            heightStack.pop()
            leftIndex = heightStack[-1] if len(heightStack) > 0 else -1
            area = currentItemHeight * (rightIndex - leftIndex - 1)
            maxArea = max(area, maxArea)
           
        return maxArea
