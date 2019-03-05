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

    def onePassInert(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        #we fill intervals strickly less the new and larger than new
        left, right = [], []
        for i in intervals:
            if i.end < s:
                left += i,
            elif i.start > e:
                right += i,
            #we face over lap situation, we keep getting the min and max for the actual start and end position
            else:
                s = min(s, i.start)
                e = max(e, i.end)
        return left + [Interval(s, e)] + right


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
    #keep 2 index
    #checkIndex
    #returnIndex
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        if len(intervals) <= 1:
            return intervals
        # for interval in intervals:
        #     print(interval.start)
        returnI = 0
        checkingI = 1
        while checkingI < len(intervals):
            #print("{0} {1}".format(returnI, checkingI))
            #do not over lap, we update the new not overlap interval
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


#practice
class Solution:
    #keep 2 index
    #checkIndex
    #returnIndex
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        if len(intervals) == 0:
            return [newInterval]
        originalL = len(intervals)
        for i in range(len(intervals)):
            if newInterval.start < intervals[i].start:
                intervals.insert(i, newInterval)
                break
        if originalL == len(intervals):
            intervals.append(newInterval)
        return self.merge(intervals)
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        checkI = 1
        returnI = 0
        if len(intervals) <= 1:
            return intervals
        while checkI < len(intervals):
            if intervals[checkI].start > intervals[returnI].end:
                #not overlap, we move on, and copy checkI interval to returnI interval
                returnI += 1
                intervals[returnI].start = intervals[checkI].start
                intervals[returnI].end = intervals[checkI].end
                checkI += 1
            else:
                newIntervalEnd = max(intervals[returnI].end, intervals[checkI].end)
                intervals[returnI].end = newIntervalEnd
                checkI += 1
        return intervals[:returnI + 1]
