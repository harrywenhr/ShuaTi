https://leetcode.com/problems/frog-jump/

#make a hashmap such that, key is the store unit position in river
#value is possible ks (jump sizes we can do at this store)
#if key + k = last store Unit, we return true

#its like recursively we land on a stone, we check all possible next stones
#so on and so forth, for DP, if no strategy, go for recusive first

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) <= 1:
            return True
        lastStoneUnitPosition = stones[-1]
        stoneMap = {}
        stoneMap[stones[0]] = set([1])
        for i in range(1, len(stones) - 1):
            stoneMap[stones[i]] = set()

        for i in range(len(stones) - 1):
            currentStone = stones[i]
            for jumpsize in stoneMap[currentStone]:
                nextStone = currentStone + jumpsize
                if nextStone == lastStoneUnitPosition:
                    return True
                #we can jump to next stone
                if nextStone in stoneMap:
                    #we update the possible jump size at next stone
                    nextJumpSizes = [jumpsize - 1, jumpsize, jumpsize + 1]
                    for nextJump in nextJumpSizes:
                        if nextJump > 0:
                            stoneMap[nextStone].add(nextJump)
        return False

