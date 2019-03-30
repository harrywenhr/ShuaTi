https://leetcode.com/problems/generate-parentheses/
Given n pairs of parentheses, write a function to generate 
all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        #left is left ( unused, right is right unused
        def dfs(left, right, currentStr, results):
            if left > right:
                return
            if left == 0 and right == 0:
                results.append(''.join(currentStr))
            else:
                if left > 0:
                    currentStr.append("(")
                    dfs(left - 1, right, currentStr, results)
                    del currentStr[-1]
                if right > 0:
                    currentStr.append(")")
                    dfs(left, right - 1, currentStr, results)
                    del currentStr[-1]
        results = []
        currentStr = []
        dfs(n, n, currentStr, results)
        return results

