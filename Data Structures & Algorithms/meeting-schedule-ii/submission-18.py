"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0 
        rooms = 1
        intervals.sort(key = lambda intervals:intervals.start)
        endDays = [intervals[0].end]
        print(endDays)

        for i in range(1,len(intervals)):
            if endDays[0]>intervals[i].start:
                rooms+=1
            else:
                heapq.heappop(endDays)
            heapq.heappush(endDays, intervals[i].end)
        return rooms



        