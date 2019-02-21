https://leetcode.com/problems/rotate-image/
class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(0, len(matrix)):
            for column in range(len(matrix[0])):
                if column > row:
                    matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
        for row in range(0, len(matrix)):
            self.swapRows(matrix[row])
    def swapRows(self, rowArray):
        for i in range(0, len(rowArray) // 2):
            rowArray[i], rowArray[-1 - i] = rowArray[-1 - i], rowArray[i]

