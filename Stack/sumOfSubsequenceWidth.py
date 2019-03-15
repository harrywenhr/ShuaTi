https://leetcode.com/problems/sum-of-subsequence-widths/
https://leetcode.com/problems/sum-of-subsequence-widths/discuss/161267/C%2B%2BJava1-line-Python-Sort-and-One-Pass


result = 
(A[high] - A[low]) * number of subsequence (which A[high] is max, A[low] is min)

= A[High] * number of subsequence (A[high] is max) - A[low] * number of sequence(A[low] is min)

class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        res = 0
        n = len(A)
        for i in range(n):
            res = res + (1 << i) * A[i] - (1 << (n - i - 1)) * A[i]
        return res % (10**9 + 7)