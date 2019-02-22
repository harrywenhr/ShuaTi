#Use number as dominations, DFS


#Dp
#We put number of combinations at n to target k As Combi(n, k)
#value at n as a[n]
#Combi(n, k) = Combi(n - 1, k) + Combi(n, k - a[n]) and add a[n] at end of those results



#Combo(k) = combo (k - a[0]) + combo (k - a[1]) + combo (k - a[2]) ...... combo (k - a[n])

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()

        return self.recusiveGetCombo(candidates, target)

        # dp = []
        # # run through all target from 1 to target
        # for i in range(1, target + 1):
        #     # run through all candidates which is smaller than i
        #     new_dp = []
        #     #for each target we try all candidates in ascending order
        #     for j in range(len(candidates)):
        #         # skip candidate which is larger than current target
        #         if candidates[j] > i:
        #             break
        #         # special case
        #         if candidates[j] == i:
        #             new_dp.append([candidates[j]])
        #         else:
        #             if i - candidates[j] > 0:
        #                 newTarget = i - candidates[j]
        #                 newTargetIndex = newTarget - 1
        #                 for comb in dp[newTargetIndex]:
        #                     #make sure list is in asceding order, prevent duplicates in final output
        #                     if candidates[j] >= comb[-1]:
        #                         newCombo = comb + [candidates[j]]
        #                         new_dp.append(newCombo) 
        #                 #new_dp.extend(comb + [candidates[j]] for comb in dp[newTargetIndex] if candidates[j] >= comb[-1])
        #     dp.append(new_dp)
            
        # return dp[-1]

#We also only append candidates to combo if it is >= to prevent duplicates
    def recusiveGetCombo(self, candidates, target):
        currentCombos = []
        for i in range(len(candidates)):
            if candidates[i] > target:
                continue
            if candidates[i] == target:
                currentCombos.append([candidates[i]])
            else:
                newTarget = target - candidates[i]
                previousCombos = self.recusiveGetCombo(candidates, newTarget)
                for combo in previousCombos:
                    if combo[-1] <= candidates[i]:
                        newCombos = combo + [candidates[i]]
                        currentCombos.append(newCombos)
        return currentCombos

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


