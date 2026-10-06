"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #input: array of intervals [start,end]
        #output: minimum number of meeting rooms to schedule all meetings

        #array of meeting times where values are [start,end]
        #find minimum number of rooms to schedule all meetings without conflict

        #pointers throughout intervals
        #so we don't exactly need to couple the start and end times
        #so we can have two lists, one for starts and one for endings

        #0 5 15
        #10 20 40

        #have start and end pointers at 0
        #move start up when less than curr end and inc counter
        #move end up when less than curr start and dec counter
        #whenever a pointer goes out of range, exit loop

        #constraints:
        #can have no meetings
        #inputs wont come sorted

        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])
        answer, rooms, startptr, endptr = 0, 0, 0, 0

        while startptr < len(intervals):
            if starts[startptr] < ends[endptr]:
                startptr+=1
                rooms+=1
            else:
                endptr+=1
                rooms-=1
            
            answer = max(answer, rooms)

        return answer