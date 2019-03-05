def mergeSort(nums):
	mergerSortHelper(nums, 0, len(nums) - 1)

def mergerSortHelper(nums, low, high):
	mid = low + (high - low) // 2
	if low < high:
		mergerSortHelper(nums, low, mid)
		mergerSortHelper(nums, mid + 1, high)
		merge(nums, low, mid, high)

def merge(nums, low, mid, high):
	print("{0} {1} {2}".format(low, mid, high))
	if low == high:
		return
	tempA = [0] * (high - low + 1)
	#merge 2 sorted list here
	leftIndex = low
	rightIndex = mid + 1
	for i in range(len(tempA)):
		#nothing on left part, we copy from right index
		if leftIndex > mid:
			tempA[i] = nums[rightIndex]
			rightIndex += 1
		elif rightIndex > high:
			#nothing on right, we copy from left index
			tempA[i] = nums[leftIndex]
			leftIndex += 1
		else:
			#we have item on both sides, we copy the smaller one
			if nums[leftIndex] <= nums[rightIndex]:
				tempA[i] = nums[leftIndex]
				leftIndex += 1
			else:
				tempA[i] = nums[rightIndex]
				rightIndex += 1
	#we now copy back from tempA to nums
	for i in range(len(tempA)):
		nums[low + i] = tempA[i]

testA = [12, 11, 13, 5, 6, 7]
mergeSort(testA)
print(testA)