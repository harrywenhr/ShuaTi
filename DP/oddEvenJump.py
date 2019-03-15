https://leetcode.com/problems/odd-even-jump/
odd jumper higher   closet
even jumper lower    closet
one higher, one lower jump alternatively, we must start with higher jump
need to get the next higher and next smaller number


need a map such that for given key, we get the nextHigher/lower key, and use
it to get the corresponding index in array, TreeMap, floorkey ceiling key

in python we sort array with index value, and use monotonic stack




class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        #for number at index i, the next higher number index
        nextHigher = self.nextClosetLarger(A)
        nextSmaller = self.nextClosetSmaller(A)
        #True if current jump is a odd jump and we can reach end
        oddJumpGoodIndexs = [False] * len(A)
        evenJumpGoodIndexs = [False] * len(A)

        oddJumpGoodIndexs[-1] = True
        evenJumpGoodIndexs[-1] = True

        validOddJumps = 1

        for i in range(len(A) - 2, -1, -1):
            #can we find next higher jump?
            nextH = nextHigher[i]
            oddJumpGoodIndexs[i] = evenJumpGoodIndexs[nextH] if nextH >= 0 else False
            nextS = nextSmaller[i]
            evenJumpGoodIndexs[i] = oddJumpGoodIndexs[nextS] if nextS >= 0 else False

            if oddJumpGoodIndexs[i]:
                validOddJumps += 1
        return validOddJumps 




    def nextClosetSmaller(self, arr):
        items = []
        for index, value in enumerate(arr):
            items.append([value, index])
        #sort reversely
        sortedItems = sorted(items, key = lambda item:item[0], reverse=True)
        stack = []
        res = {}
        for item in sortedItems:
            itemIndex = item[1]
            while stack and stack[-1] < itemIndex:
                prevIndex = stack.pop()
                res[prevIndex] = itemIndex
            stack.append(itemIndex)
        while stack:
            res[stack.pop()] = -1
        return res
    def nextClosetLarger(self, arr): 
        #dont use map as it can not handle duplicates
        items = []
        for index, value in enumerate(arr):
            items.append([value, index])
        #print(mapIndex)
        sortedItems = sorted(items, key = lambda item:item[0])
        #print(sortedMap)
        #we travel from small to large, use index to keep a descending stack
        #So if we can pop one, means current index is larger, and current value is
        #just a bit larger than stack peek value, then for each poped index
        #we know its next larger item to the right
        #new item is larger than in stack, the Desending stack means that when we pop a 
        #stack item, its index is smaller than current, and we found or closet item to
        #the right
        stack = []
        #key is the current item index, value is the next larger and closet item index 
        res = {}
        for item in sortedItems:
            itemIndex = item[1]
            while stack and stack[-1] < itemIndex:
                #prevIndex is less than item index, and itemValue is also smaller
                prevIndex = stack.pop()
                res[prevIndex] = itemIndex
            stack.append(itemIndex)
        #if item does not have larger item on the right, it will not be saved in res
        #print(res)
        #print(stack)
        while stack:
            res[stack.pop()] = -1
        return res