
https://leetcode.com/problems/median-of-two-sorted-arrays/


Dividing a set into two equal length subsets, that one subset is always greater than the other.

!!!!!!!!!!!
m,n list
use cutting index i and j
make sure we
left part of m (m[0]~m[i-1]) + left part of n (n[0] ~n[j-1]) =
right part of m (m[i] ~ m[m-1]) + right part of n (n[j] ~ n[n -1])
!!!!!!!!!!!!

also
max(m[i-1], n[j-1]) <= min (m[i], n[j])

Median = (max(m[i-1], n[j-1]) + min (m[i], n[j]) ) / 2 if m + n is even

max(m[i-1],  n[j-1]) if m + n is odd


i from 0 ~ m

i + j = m - i + n - j => j = (m + n) / 2 - i    if m + n is even
j need >=0 means n >= m

i + j = m - i + n - j + 1 => j = (m + n + 1) / 2 - i if m + n is odd we keep one more at left part
j need >=0 means n + 1 >= m 

!!!!!!!!!!combined we always do n >= m 

find a i in 0 ~ m 
such that 
m[i-1] <= n[i] always true
m[i-1] <= n[j]
n[j-1] <= n[j] always true
n[j-1] <= m[i]


m[i-1] <= n[j] and
n[j-1] <= m[i]

!!!!!!!!
if i = 0, means there is no left part of list m , we dont need to satisfy m[i-1] <= n[j]
same thing for j = n, means no right part of list n, dont need to satisfy


if j = 0, means there is no left part of list n, we dont need to satisfy n[j-1] > m[i]
same thing got i = m, means there is no right part of list m, dont need to satisfy

if m[i-1] > n[j] we decrease i
if n[j-1] > m[i] we increase i

if i = 0 or j = n or m[i -1] <= n[j]

and j = 0 or i = m or m[j-1] <= m[i]
!!!!!!!!!
we found our median, 


import statistics
class Solution:
	def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
		#make sure nums2 len >= nums1
		if len(nums1) > len(nums2):
			nums1, nums2 = nums2, nums1
		if len(nums1) == 0:
			return statistics.median(nums2)
		if len(nums2) == 0:
			return statistics.median(nums1)
		#search range
		ALeft = 0
		ARight = len(nums1)
		isOdd = False
		if ((len(nums1) + len(nums2)) % 2) == 1:
			isOdd = True
		#return self.recursiveFind(ALeft, ARight, nums1, nums2, isOdd)
		return self.loopFind(ALeft, ARight, nums1, nums2, isOdd)
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
	
	def loopFind(self, ALeft, ARight, nums1, nums2, isOdd):
		while ALeft <= ARight:
			cutA = (ALeft + ARight)
			cutB = (len(nums1) + len(nums2)) // 2 - cutA
			if isOdd:
				cutB = (len(nums1) + len(nums2) + 1) // 2 - cutA
			#we got our median, if we are at edge, we automatically satisfied the condition as there's nothing to compare
			if (	(cutA == 0 or cutB == len(nums2) or nums1[cutA - 1] <= nums2[cutB]) 
				and (cutB == 0 or cutA == len(nums1) or nums2[cutB - 1] <= nums1[cutA])
				):
				#we get the rightmost on left basket, left most on right basket, watchout for edge cases
				ALeftLarge = nums1[cutA - 1] if cutA > 0 else nums2[cutB - 1]
				BLeftLarge = nums2[cutB - 1] if cutB > 0 else ALeftLarge
				ARightSmall = nums1[cutA] if cutA < len(nums1) else nums2[cutB]
				BRightSmall = nums2[cutB] if cutB < len(nums2) else ARightSmall
				if isOdd:
					return float(max(ALeftLarge, BLeftLarge))
				return float((max(ALeftLarge, BLeftLarge) + min(ARightSmall, BRightSmall)) / 2)
			elif cutA > 0 and nums1[cutA - 1] > nums2[cutB]:
				#Since we operate on small list, if cutA > 0, cutB cant be len(nums2), otherwise we have too many in left basket
				#cutA is too right, we decrease
				ARight = cutA - 1
			elif cutA < len(nums1) and nums2[cutB - 1] > nums1[cutA]:
				#Since A is smaller then B, we always need some element from B, cutB cant be 0
				#cutA is too Left, we increase
				ALeft = cutA + 1	

	def recursiveFind(self, ALeft, ARight, nums1, nums2, isOdd):
		#in python 3 we use // to get int divisions 
		cutA = (ALeft + ARight) // 2
		cutB = (len(nums1) + len(nums2)) // 2 - cutA

		if isOdd:
			cutB = (len(nums1) + len(nums2) + 1) // 2 - cutA
		#median found situation
		if (cutA == 0 or cutB == len(nums2) or nums1[cutA - 1] <= nums2[cutB]) and (cutB == 0 or cutA == len(nums1) or nums2[cutB - 1] <= nums1[cutA]):
			#if theres no index left on cutA or cutA, we make them the same as the other one for later min max operations
			ALeftLarge = nums1[cutA - 1] if cutA > 0 else nums2[cutB - 1]
			BLeftLarge = nums2[cutB - 1] if cutB > 0 else ALeftLarge
			ARightSmall = nums1[cutA] if cutA < len(nums1) else nums2[cutB]
			BRightSmall = nums2[cutB] if cutB < len(nums2) else ARightSmall
			if isOdd:
				return float(max(ALeftLarge, BLeftLarge))
			return float((max(ALeftLarge, BLeftLarge)+ min(ARightSmall, BRightSmall))) / 2.0
		elif cutA > 0 and cutB < len(nums2) and nums1[cutA - 1] > nums2[cutB]:
			#cutA is too right, we narraw the search range to left
			ARight = cutA - 1
			return self.recursiveFind(ALeft, ARight, nums1, nums2, isOdd)
		elif cutB > 0 and cutA < len(nums1) and nums2[cutB - 1] > nums1[cutA]:
			#cutA is too left, we narraw the search range to right
			ALeft = cutA + 1
			# print "ALeft {}".format(ALeft)
			# print "ARight {}".format(ARight) 
			return self.recursiveFind(ALeft, ARight, nums1, nums2, isOdd)


#practice

#cut with smalled array
#median means evenly divide elements, all left part is less then right part
#binary search to cut

array m, array n 

m left part is [Aleft to Acut)
m right part is [Acut, Aright]

Bcut = (len(m) + len(n)) // 2 - Acut if even
(len(m) + len(n) + 1) // 2 - Acut + if odd
import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #make sure nums2 len >= nums1
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        if len(nums1) == 0:
            return statistics.median(nums2)
        if len(nums2) == 0:
            return statistics.median(nums1)
        m = len(nums1)
        n = len(nums2)
        isOdd = True if ((m + n) % 2 == 1) else False
        #we cut from 0 to end of length, 0 means nothing on left,
        # length means nothing on right
        Aleft = 0
        Aright = len(nums1)
        #handles when there's only one element
        while Aleft <= Aright:
            #print(Aleft)
            #print(Aright)
            Acut = Aleft + (Aright - Aleft) // 2
            Bcut = (m + n) // 2 - Acut
            if isOdd:
                Bcut = (m + n + 1) // 2 - Acut
            #print("{0} {1}".format(Acut, Bcut))
            AleftLarge = nums1[Acut - 1] if Acut >= 1 else -sys.maxsize
            BleftLarge = nums2[Bcut - 1] if Bcut >= 1 else -sys.maxsize
            ArightSmall = nums1[Acut] if Acut < m else sys.maxsize
            BrightSmall = nums2[Bcut] if Bcut < n else sys.maxsize
            #valid the invariant
            leftSideMax = max(AleftLarge, BleftLarge)
            rightSideMin = min(ArightSmall, BrightSmall)
            if leftSideMax <= rightSideMin:
                finalMedian = float((leftSideMax + rightSideMin)) / 2.0
                if isOdd:
                    finalMedian = float(leftSideMax)
                return finalMedian
            else:
                #we have small items on the right side
                #whoever is smaller on left part, we cut more to bring 
                #small items from right side
                if AleftLarge <= BleftLarge:
                    #move Acut to right
                    Aleft = Acut + 1
                    #print("Aleft {}".format(Aleft))
                else:
                    #move Acut to left
                    Aright = Acut - 1






			