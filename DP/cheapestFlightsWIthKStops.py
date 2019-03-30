https://leetcode.com/problems/cheapest-flights-within-k-stops/

# Time Complexity: O(E + n \log n)O(E+nlogn), where EE is the total number of flights.

# Space Complexity: O(n)O(n), the size of the heap.

# from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        adjacencyMap = defaultdict(dict)
        for flight in flights:
            departure = flight[0]
            destination = flight[1]
            cost = flight[2]
            #if does not exists we will create a empty dict and set the key
            adjacencyMap[departure][destination] = cost
        #distanceToSrc, vertex, pathLengh
        minQ = [(0,src,0)]
        while minQ:
            currentItem = heapq.heappop(minQ)
            distanceToSrc, vertex, pathLengh = currentItem[0], currentItem[1], currentItem[2]
            #check if we are at end, if so, record current shortest cost and return
            if vertex == dst:
                return distanceToSrc
            #check neighbors
            #we can still add one more segement
            if pathLengh <= K:
                for adjacentVertex in adjacencyMap[vertex]:
                    cost = adjacencyMap[vertex][adjacentVertex]
                    newCost = distanceToSrc + cost
                    newItem = (newCost, adjacentVertex, pathLengh + 1)
                    heapq.heappush(minQ, newItem)
        return -1