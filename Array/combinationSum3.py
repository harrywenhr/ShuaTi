https://leetcode.com/problems/combination-sum-iii/

Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

#same, we either pick a number or we dont

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        result = []
        self.helper(k, n, 1, path, result)
        return result
    #number from 1-9
    def helper(self, currentK, currentN, number, path, result):
        #we used all numbers, if we match the sum, we add it
        if currentK == 0:
            if currentN == 0:
                newPath = list(path)
                result.append(newPath)
        else:
            #we are overflow, we return
            if currentN <= 0:
                return
            #we recusively Find
            for candidateNumber in range(number, 10):
                path.append(candidateNumber)
                self.helper(currentK - 1, currentN - candidateNumber, candidateNumber + 1, path, result)
                del path[-1]