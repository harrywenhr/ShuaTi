https://leetcode.com/problems/triangle/


dp[i,j] = min path sum at row i, coloum j
dp[i,j] = min(dp[i - 1, j], dp[i - 1, j - 1]) + t[i,j]

currentRow[j] = min(previousRow[j], previousRow[j-1]) + t[j]

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        previousRow = triangle[0]
        for i in range(1, len(triangle)):
            currentRow = []
            for j in range(len(triangle[i])):
                prevsCase1 = previousRow[j] if j < i else sys.maxsize
                prevsCase2 = previousRow[j - 1] if j >= 1 else sys.maxsize
                currentMin = min(prevsCase1, prevsCase2) + triangle[i][j]
                currentRow.append(currentMin)
            previousRow = currentRow
            #print(currentRow)
        return min(currentRow)
