"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda  i : i.start)
        if len(intervals)<=1:
            return True
        heapp = []
        heapq.heappush(heapp,intervals[0].end)
        for i in range(1,len(intervals)):
            if intervals[i].start<heapp.pop():
                return False
            heapq.heappush(heapp,intervals[i].end)
        return True
            
            

