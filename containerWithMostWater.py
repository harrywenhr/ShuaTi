
greedy apoarch, 2 pointers at start and end, we always move the shorter line pointer as it may result in a larger area
class Solution:
	def maxArea(self, height: 'List[int]') -> 'int':
		if len(height) <= 1:
			return 0
		leftI = 0
		rightI = len(height) - 1
		maxArea = 0
		while leftI < rightI:
			#left is short, we move left one
			if height[leftI] < height[rightI]:
				currentArea = height[leftI] * (rightI - leftI)
				maxArea = max(maxArea, currentArea)
				leftI += 1
			else:
				currentArea = height[rightI] * (rightI - leftI)
				maxArea = max(maxArea, currentArea)
				rightI -= 1
		return maxArea