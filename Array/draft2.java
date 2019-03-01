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