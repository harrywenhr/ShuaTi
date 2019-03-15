https://leetcode.com/problems/sort-array-by-parity/

Given an array A of non-negative integers, 
return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

#We use 2 pointers, even and odd, when find it we swap
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evenI = 0
        oddI = len(A) - 1
        while (evenI < oddI):
            while evenI < oddI and A[evenI] % 2 == 0:
                evenI += 1
            while evenI < oddI and A[oddI] % 2 == 1:
                oddI -= 1
            #we do the swap here
            if evenI < oddI:
                A[evenI], A[oddI] = A[oddI], A[evenI]
                evenI += 1
                oddI -= 1
        return A

#practiced