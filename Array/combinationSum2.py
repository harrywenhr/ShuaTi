https://leetcode.com/problems/combination-sum-ii/
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.


for each number, we pick it or we dont pick it

    // O(k * 2^n) time:
    // 每个解的长度平均为k, copy list的时间复杂度是O(k)
    // 解空间:
    // 因为元素只能用一次, 所以对于长度是k的解, 解的个数最多是C(n,k)个, 而一般情况下, 
    // 解的个数远小于C(n,k), 那么问题来了, 对于长度为k的解, worst case是什么？
    // int[] arr = {1,1,1,1,1,1,1,1,1,1}  target = 2 这时候解的个数才达到C(n,k),
    // 注意: 即便在ret.add之前要去重, 我们也是在找到了可行解之后再检查是否是重复解, 所以
    //      解空间树是包含重复解的, 所以时间复杂度也包括这些重复解
    //
    // 还有一点是, 题解的长度并不是固定的, 也就是k可能有多个, 所以可能是C(n,0) ~ C(n,n)
    // 中的多个之和, 而我们知道C(n,0) + C(n,1) + C(n,2) + ... C(n,n) = 2^n
    // 所以可以把时间复杂度算成O(k * 2^n)

    if treat copy path to result as O(1)
    we have 2^n


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []
        self.helper(candidates, target, 0, path, result)
        return result
    def helper(self, candidates, target, index, path, result):
        if target == 0:
            newPath = list(path)
            result.append(newPath)
            #print("return1")
        elif target < 0:
            #print("return2")
            return
        else:
            #for every index item, we either pick it or we dont
            #we only pick new item to prevent duplicates
            for i in range(index, len(candidates)):
                if i == index or candidates[i] != candidates[i - 1]:
                    #newPath = path + [candidates[i]]
                    path.append(candidates[i])
                    self.helper(candidates, target - candidates[i], i + 1, path, result)
                    #we unpick the current item, always make sure we unpick the current one after recursion
                    del path[-1]