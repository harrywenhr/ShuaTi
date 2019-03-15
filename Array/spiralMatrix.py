#https://leetcode.com/problems/spiral-matrix/
#We have a helper function that prints one single loop
#Careful not print duplicates on corners
#each time a smaller loop is -2!!! in terms of width and height compared to previous one
# base case is n = 1 or m = 1, we simply print the remaining ones
class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        n = len(matrix)
        if n < 1:
            return []
        m = len(matrix[0])
        if m < 1:
            return []
        startX = startY = 0
        result = []
        while (m > 0 and n > 0):
            if m == 1:
                for y in range(startY, startY + n):
                    result.append(matrix[y][startX])
                break
            elif n == 1:
                for x in range(startX, startX + m):
                    result.append(matrix[startY][x])
                break
            self.getSingleLoop(matrix, startX, startY, m, n, result)
            startX += 1
            startY += 1
            m -= 2
            n -= 2
        return result
    def getSingleLoop(self, matrix, startX, startY, m, n, result):
        for x in range(startX, startX + m):
            result.append(matrix[startY][x])
        for y in range(startY + 1, startY + n):
            result.append(matrix[y][startX + m - 1])
        for x in range(startX + m - 2, startX - 1, -1):
            result.append(matrix[startY + n - 1][x])
        for y in range(startY + n - 2, startY, -1):
            result.append(matrix[y][startX])

#practiced
