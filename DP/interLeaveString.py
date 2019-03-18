https://leetcode.com/problems/interleaving-string/
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

result(x,y,z) = result(x, y - 1, z - 1) or result(x - 1, y, z - 1)

baseCase
result(x,0,z) = strS == strZ
result(0,y,z) = strS == strZ

z = x + y


#use length to calculate dpTable
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1) + len(s2)) != len(s3):
            return False
        dpTable = [[False for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        for x in range(len(s1) + 1):
            for y in range(len(s2) + 1):
                z = x + y
                if x == 0 and y == 0:
                    dpTable[x][y] = True
                elif x == 0:
                    dpTable[x][y] = (s2[:y] == s3[:z])
                elif y == 0:
                    dpTable[x][y] = (s1[:x] == s3[:z])
                else:
                    if s3[z - 1] == s1[x - 1] == s2[y - 1]:
                        dpTable[x][y] = dpTable[x - 1][y] or dpTable[x][y - 1]
                    elif s3[z - 1] == s1[x - 1]:
                        dpTable[x][y] = dpTable[x - 1][y]
                    elif s3[z - 1] == s2[y - 1]:
                        dpTable[x][y] = dpTable[x][y - 1]
                    else:
                        dpTable[x][y] = False
        #print(dpTable)
        return dpTable[-1][-1]

    #we only need the previous item on same row and previous row to get dpTable[x][y]
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:    
        if (len(s1) + len(s2)) != len(s3):
            return False
        previousRow = [False for i in range(len(s2) + 1)]
        currentRow = [False for i in range(len(s2) + 1)]
        for x in range(len(s1) + 1):
            for y in range(len(s2) + 1):
                z = x + y
                if x == 0:
                    #first row
                    currentRow[y] = (s2[:y] == s3[:z]) if y > 0 else True
                else:
                    #following rows
                    if y == 0:
                        currentRow[y] = (s1[:x] == s3[:z]) if x > 0 else True
                    else:
                        if s3[z - 1] == s1[x - 1] == s2[y - 1]:
                            currentRow[y] = currentRow[y - 1] or previousRow[y]
                        elif s3[z - 1] == s1[x - 1]:
                            currentRow[y] = previousRow[y]
                        elif s3[z - 1] == s2[y - 1]:
                            currentRow[y] = currentRow[y - 1]
                        else:
                            currentRow[y] = False
            previousRow = currentRow
        return currentRow[-1]
