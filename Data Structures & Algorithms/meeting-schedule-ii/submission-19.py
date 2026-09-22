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
        intervals.sort(key= lambda intervals:intervals.start)
        endmeetings = [intervals[0].end]
        rooms = 1

        for i in range(1,len(intervals)):
            if endmeetings[0]>intervals[i].start:
                rooms+=1
            else:
                heapq.heappop(endmeetings)
            heapq.heappush(endmeetings,intervals[i].end)
        return rooms


            



        