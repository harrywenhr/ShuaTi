https://leetcode.com/problems/daily-temperatures/
#days till a warmer temperature
#keep a descending stack, when poping out, a warmer day arrived
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ascendingStack = []
        #store index in stack
        for i in range(len(T)):
            #we have a warmer day for current stack peek
            while ascendingStack and T[ascendingStack[-1]] < T[i]:
                prevIndex = ascendingStack.pop()
                T[prevIndex] = i - prevIndex
            ascendingStack.append(i)
        while ascendingStack:
            prevIndex = ascendingStack.pop()
            T[prevIndex] = 0
        return T