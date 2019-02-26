https://leetcode.com/problems/insert-interval/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

#scan through intervals till newStart > currentStart
#insert our new interval
# merge intervals 

class Solution:
    def print(self, intervals):
        for interval in intervals:
            print(" {0},{1} ".format(interval.start, interval.end))
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        originalLength = len(intervals)
        for i in range(len(intervals)):
            #we insert new one after current one to keep it sorted
            if newInterval.start < intervals[i].start: 
                #print(i)
                intervals.insert(i, newInterval)
                break
        if originalLength == len(intervals):
            intervals.append(newInterval)
        #self.print(intervals)
        return self.merge(intervals)

    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        if len(intervals) <= 1:
            return intervals
        # for interval in intervals:
        #     print(interval.start)
        returnI = 0
        checkingI = 1
        while checkingI < len(intervals):
            #print("{0} {1}".format(returnI, checkingI))
            #do not over lap, we update the new ont overlap interval
            if intervals[returnI].end < intervals[checkingI].start:
                returnI += 1
                intervals[returnI] = intervals[checkingI]
                checkingI += 1
            #overlap
            else:
                #we update end value
                if intervals[returnI].end < intervals[checkingI].end:
                    intervals[returnI].end = intervals[checkingI].end
                #we do not need to update returnI in this case
                checkingI += 1
        returnI += 1
        return intervals[:returnI]