"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda intervals:intervals.start)
        rooms = 1
        if not intervals:
            return 0
        endTimes = [intervals[0].end]

        for i in range(1,len(intervals)):
            lastEnd = endTimes[0]
            if lastEnd>intervals[i].start:
                rooms+=1
            else:
                heapq.heappop(endTimes)
            heapq.heappush(endTimes,intervals[i].end)
            
        return rooms





        