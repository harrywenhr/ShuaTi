https://leetcode.com/problems/maximal-square/

#SQUARE!!! not rectangle


a SQUARE of length 3 with bottom right at (2,2)

1 1 1
1 1 1
1 1 1

(2,1) square length must be >= 2

(1,2) square length must be >= 2

(1,1) square length must be >= 2

otherwise we cant fill square at (2,2)


for square with length x, all 3 previous square must have length >= x - 1
so if previous squire has length x,y,z then next square will be min(x,y,z) + 1


#can also use a 1d array as we only use previous row and previous element
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        maxR = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                #current square length = min(x,y,z) + 1 if
                if matrix[i][j] == '1':
                    case1 = int(matrix[i - 1][j]) if i > 0 else 0
                    case2 = int(matrix[i][j - 1]) if j > 0 else 0
                    case3 = int(matrix[i - 1][j - 1]) if (i * j) > 0 else 0
                    squareL = min(case1, case2, case3) + 1
                    maxR = max(maxR, squareL **2)
                    matrix[i][j] = str(squareL)
        return maxR
