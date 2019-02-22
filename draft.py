#Use number as dominations, DFS


#Dp
#We put number of combinations at n to target k As Combi(n, k)
#value at n as a[n]
#Combi(n, k) = Combi(n - 1, k) + Combi(n, k - a[n]) and add a[n] at end of those results


class Solution:
    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        # result = self.getCombinations(candidates, len(candidates) - 1, target)
        # if not result:
        #     return []
        # return result
        result = self.getCombinationsDP(candidates, target)
        return result

    def getCombinationsDP(self, candidates, target):
        # target is 0 to target
        emptyResult = [[]]
        dpTable = [[ emptyResult for n in range(len(candidates))] for row in range(target + 1)]
        #row here is target
        for row in range(1, target + 1):
            #columnn here is index
            for column in range(len(candidates)):
                combinations1 = dpTable[row][column - 1] if column >= 1 else None
                newTarget = row - candidates[column]
                combinations2 = dpTable[newTarget][column] if newTarget >= 0 else None
                #print(dpTable)
                #print("{0} {1} {2}".format(row, candidates[column], newTarget))
                if not combinations1 and not combinations2:
                    dpTable[row][column] = None
                    continue
                if not combinations2:
                    dpTable[row][column] = combinations1
                    continue
                for combo in combinations2:
                    combo.append(candidates[column])
                if not combinations1:
                    dpTable[row][column] = combinations2
                    continue
                if combinations1 and combinations2:
                    dpTable[row][column] = combinations1 + combinations2
        return dpTable[target][len(candidates) - 1]

    def getCombinations(self, candidates, index, target):
        if target == 0:
            return [[]]
        if target < 0:
            return None
        if index < 0 and target > 0:
            return None
        combinations1 = self.getCombinations(candidates, index - 1, target)
        combinations2 = self.getCombinations(candidates, index, target - candidates[index])
        if not combinations1 and not combinations2:
            return None
        if not combinations2:
            return combinations1
        for combo in combinations2:
            combo.append(candidates[index])
        if not combinations1:
            return combinations2
        return combinations1 + combinations2


