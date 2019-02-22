https://leetcode.com/problems/combination-sum/

#Use number as dominations, DFS


#Dp

class Solution:
    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':












        #candidates.sort()
        result = []
        currentSelected = []
        if not candidates:
            return result.append([])
        self.dfsCalculate(candidates, 0, target, currentSelected, result)
        return result
    def dfsCalculate(self, candidates, checkingIndex, target, currentSelected, result):
        #print("{0} {1} {2} {3}".format(checkingIndex, currentSelected, target, result))
        if target == 0:
            result.append(currentSelected.copy())
            return
        if checkingIndex == len(candidates):
            return
        domination = 0
        while ((domination * candidates[checkingIndex]) <= target):
            newTarget = target
            if domination > 0:
                newTarget = newTarget - candidates[checkingIndex] * domination
                currentSelected.append(candidates[checkingIndex])
            self.dfsCalculate(candidates, checkingIndex + 1, newTarget, currentSelected.copy(), result)
            domination += 1