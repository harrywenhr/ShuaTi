https://leetcode.com/problems/longest-valid-parentheses/

from left to right, we maintain invariant left parenthese >= right parenthese, if right is more, its not a valid starting point
we reset count, when right catches left, we calculate the length

{{{{{{}}}}}

but there's a change right never catches up, so we scan backwards
from right to left, maintain invaiant right >= left, if left is more, we reset count
when left catches up with right, we calculate the length


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        leftCount = 0
        rightCount = 0
        maxLength = 0
        for i in range(len(s)):
            if s[i] == '(':
                leftCount += 1
            else:
                rightCount += 1
            #now we check our invaiant
            if leftCount == rightCount:
                maxLength = max(maxLength, leftCount * 2)
            elif rightCount > leftCount:
                #reset
                rightCount = 0
                leftCount = 0
        rightCount = 0
        leftCount = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                leftCount += 1
            else:
                rightCount += 1
            if leftCount == rightCount:
                maxLength = max(maxLength, leftCount * 2)
            elif rightCount < leftCount:
                rightCount = 0
                leftCount = 0
        return maxLength




1) Create an empty stack and push -1 to it. The first element
   of stack is used to provide base for next valid string. 

2) Initialize result as 0.

3) If the character is '(' i.e. str[i] == '('), push index 
   'i' to the stack. 
   
2) Else (if the character is ')')
   a) Pop an item from stack (Most of the time an opening bracket)
   b) If stack is not empty, then find length of current valid
      substring by taking difference between current index and
      top of the stack. If current length is more than result,
      then update the result.
   c) If stack is empty, push current index as base for next
      valid substring.


    def longestValidParentheses(self, s: str) -> int:
        #push base index
        stack = [-1]
        maxLength = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                #stack is empty, need a new starting base inde
                #current right p have no match
                if not stack:
                    stack.append(i)
                else:
                    validLength = i - stack[-1]
                    maxLength = max(maxLength, validLength)
        return maxLength