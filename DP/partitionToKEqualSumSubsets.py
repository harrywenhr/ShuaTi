https://leetcode.com/problems/partition-to-k-equal-sum-subsets/


# The key is, bucket[i] == 0 means for all j > i, sum[j] == 0; because this algorithm always fill the previous buckets before trying the next.
# So if by putting nums[i] in this empty bucket can't solve the game, putting nums[i] on other empty buckets can't solve the game either.


    #dfs, for each number, we have k choice/buckets to put, we do dfs still we have a path that matches the requirement
    def canPartitionKSubsets(self, nums, k):
        nums.sort(reverse=True) # Game Changer 1
        arrSum = sum(nums)
        bucket, kSum = [0] * k, arrSum // k
        if (arrSum % k) > 0:
            return False
        def dfs(index):
            #end case
            if index == len(nums):
                #if all sums in bucket are equal, we return true
                return len(set(bucket)) == 1
            #we put current number into k buckets
            currentNumber = nums[index]
            for i in range(k):
                if (bucket[i] + currentNumber) <= kSum:
                    #we can put current number into this bucket
                    bucket[i] += currentNumber
                    #continue dfs
                    if dfs(index + 1):
                        return True
                    #this path does not work, we remove current number
                    bucket[i] -= currentNumber
                    #if we cannot add current number into a empty bucket, then all following empty buckets will not work either
                    if bucket[i] == 0: 
                        break # Game Changer 2
            #this number cannot be add to any bucket
            return False
        return dfs(0)

    def canPartitionKSubsets(self, A, k):
        if len(A) < k:
            return False
        ASum = sum(A)
        A.sort(reverse=True)
        if ASum % k != 0:
            return False
        target = [ASum / k] * k

        def dfs(pos):
            if pos == len(A): return True
            for i in xrange(k):
                if target[i] >= A[pos]:
                    target[i] -= A[pos]
                    if dfs(pos + 1):
                        return True
                    target[i] += A[pos]
            return False
        return dfs(0)


