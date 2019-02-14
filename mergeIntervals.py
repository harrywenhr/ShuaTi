https://leetcode.com/problems/merge-intervals/solution/
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

#Sort intervals on start value
#For 0 to n - 1, merge intervals with its after ones
#remember to update the new not overlap interval

class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        intervals = sorted(intervals, key = lambda interval: interval.start)
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




