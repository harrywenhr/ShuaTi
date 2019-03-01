#https://leetcode.com/problems/maximal-rectangle/


#We transform this problem to max rectangle in histogram
#For every row in matrix, we get the max rectangle of that rows histogram
# We then will find the largest rectangle

class Solution:
    #O(N^3)
    def maximalRectangle(self, matrix: 'List[List[str]]') -> 'int':
        if len(matrix) == 0:
            return 0
        if len(matrix) == 1:
            return self.maximalRectangleInHistogram(matrix[0])
        for row in range(0, len(matrix)):
            for column in range(0, len(matrix[0])):
                matrix[row][column] = int(matrix[row][column])
                if row >= 1:
                    #add previous height to current position if we have, otherwsie leave it be
                    if (matrix[row - 1][column] > 0) and (matrix[row][column] == 1):
                        matrix[row][column] += matrix[row - 1][column]
        maxArea = 0
        for row in range(0, len(matrix)):
            currentArea = self.maximalRectangleInHistogram(matrix[row])
            maxArea = max(maxArea, currentArea)
        return maxArea
    #O(N)
    def maximalRectangleInHistogram(self, rowArray):
        if len(rowArray) == 0:
            return 0
        heightStack = []
        maxArea = 0
        for i in range(0, len(rowArray)):
            rowArray[i] = int(rowArray[i])
            #Keep a ascending stack
            if len(heightStack) == 0 or rowArray[heightStack[-1]] <= rowArray[i]:
                heightStack.append(i)
            else:
                while(len(heightStack) > 0 and rowArray[heightStack[-1]] > rowArray[i]):
                    currentItemHeight = rowArray[heightStack[-1]]
                    heightStack.pop()
                    leftIndex = heightStack[-1] if len(heightStack) > 0 else -1
                    rightIndex = i
                    currentArea = currentItemHeight * (rightIndex - leftIndex - 1)
                    maxArea = max(maxArea, currentArea)
                heightStack.append(i)
        while(len(heightStack) > 0):
            currentItemHeight = rowArray[heightStack[-1]]
            heightStack.pop()
            leftIndex = heightStack[-1] if len(heightStack) > 0 else -1
            rightIndex = len(rowArray)
            currentArea = currentItemHeight * (rightIndex - leftIndex - 1)
            maxArea = max(maxArea, currentArea)
        return maxArea

