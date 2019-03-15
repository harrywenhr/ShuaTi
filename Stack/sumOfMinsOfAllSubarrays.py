https://www.geeksforgeeks.org/sum-of-minimum-elements-of-all-subarrays/
https://leetcode.com/problems/sum-of-subarray-minimums/
https://leetcode.com/problems/sum-of-subarray-minimums/discuss/170750/C%2B%2BJavaPython-Stack-Solution

res = sum(A[i] * f(i))
where f(i) is the number of subarrays,
in which A[i] is the minimum.


To get f(i), we need to find out:
left[i], the length of strict bigger numbers on the left of A[i],
right[i], the length of bigger numbers on the right of A[i].


left[i] + 1 equals to
the number of subarray ending with A[i],
and A[i] is single minimum.

right[i] + 1 equals to
the number of subarray starting with A[i],
and A[i] is the first minimum.

Finally f(i) = (left[i] + 1) * (right[i] + 1)


Intuition on the choice of strictly bigger (i.e. greater than, >) on the 
left and bigger (i.e. greater than or equal, >=) on the right: 
We need to account for each subset exactly once. If both sides use >=, 
then some contiguous subsets, specifically those including the minimum 
number A[i] multiple times, will be accounted for more than once. 
Similarly, if both sides use >, then those subsets won't be accounted 
for at all. Therefore, either left or right side should use > and the 
other one should use >=. It doesn't matter which one. In this question 
this choice (left >, right >=) makes A[i] the "chosen" minimum such 
that it is the single (i.e. only) minimum for subsets on the left and 
the first minimum for subsets on the right. Therefore, if there are 
multiple values equal to A[i] in a subset, it will be accounted for 
exactly once.
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        mod = 10**9 + 7
        #ascend1 find first number on the left is smaller
        #ascend2 find first number on the right (scan backwards) is smaller
        #store indexs
        ascendingStack1, ascendingStack2 = [], []
        #length of bigger numbers on left 
        #length of >= numbers on right
        left, right = [0] * len(A), [0] * len(A)

        for i in range(len(A)):
            while ascendingStack1 and A[ascendingStack1[-1]] > A[i]:
                ascendingStack1.pop()
            #now peek of stack is <= A[i]
            leftStrickLargerIndex = ascendingStack1[-1] if ascendingStack1 else -1
            left[i] = i - leftStrickLargerIndex - 1
            ascendingStack1.append(i)
        #print(left)

        for i in range(len(A) - 1, -1, -1):
            while ascendingStack2 and A[ascendingStack2[-1]] >= A[i]:
                ascendingStack2.pop()
            rightLargerIndex = ascendingStack2[-1] if ascendingStack2 else len(A)
            right[i] = rightLargerIndex - i - 1
            ascendingStack2.append(i)
        #print(right)
        resSum = 0
        for i in range(len(A)):
            resSum += (left[i] + 1) * (right[i] + 1) * A[i]
        return resSum % mod



