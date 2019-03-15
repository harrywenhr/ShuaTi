#   

# Given an array with n objects colored red, white or blue, 
#sort them in-place so that objects of the same color are adjacent, 
#with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.


# Just like the Lomuto partition algorithm usually used in quick sort. 
# We keep a loop invariant that [0,i) [i, j) [j, k) are 0s, 1s and 2s 
# sorted in place for [0,k). 
# Here ")" means exclusive. We don't need to swap because we know the values we want.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for k in range(len(nums)):
            #get current value
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1


# Proof: Initialization: i=j=k=0. [0,0) [0,0) [0,0) don't exist [k=0,len(nums)-1] undetermined
# [0,i) [i, j) [j, k) are 0s, 1s and 2s
# Maintenance： Case 1:encounter 2, [0,i) [i,j) don't change [j,k)->[j,k+1)
# Case 2: encounter 0, [0, i)-> [0,i+1), [i,j)->[i+1,j+1), [j, k)->[j+1,k+1)
# Case 3: encounter 1: [0,i) doesn't change, [i,j)->[i,j+1), [j,k)->[j+1, k+1)
# Termination: The same as "Maintenance"

[0,0,0,1,1,1,2,2,2]
next one is 0
we bump 0s to 0000
bump 1s to 1111
then bump 2s to 2222
        i = j = 0
        for k in range(len(nums)):
            v = nums[k]
            if v == 0:
                #we need to bump the areas of 1s and 2s
                #we set current k to 2 first, the set current j = 1
                #then set current i to 0, 
                #expanding the areas one by one from the end
                #previous positions will be over write as the 1s and 2s 
                #area expand
                nums[k] = 2
                nums[j] = 1
                nums[i] = 0
                i += 1
                j += 1
            elif v == 1:
                #we only need to bump area 1 and 2
                nums[k] = 2
                nums[j] = 1
                j += 1
            else:
                #only need to bump area 2
                nums[k] = 2

#practiced


