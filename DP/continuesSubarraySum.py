https://leetcode.com/problems/continuous-subarray-sum/solution/
#similar thought as 2 sum, use a hash map to save (%k), and a local
#variable to save current sum
#for new sum, we check if %k exists
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #save remainder and it's local sum index, initial we have
        remainMap = {0:-1}
        localSum = 0
        #need to check if we have consective 0s, as k*0 = 0
        for i in range(len(nums)):
            number = nums[i]
            localSum += number
            remainder = (localSum % k )if k != 0 else localSum
            if remainder in remainMap:
                if (i - remainMap[remainder]) > 1:
                    return True
            else:
                remainMap[remainder] = i

        return False