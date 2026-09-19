"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #input: array of [start i, end i] where start < end
        #output: min number of rooms to have all meetings

        #overlap is exclusive

        #going to sort both start and ends into their own arrays
        #in this case the ordering doesnt need to be coupled
        #so our system is that we start and end ptr at 0
        #we move start up and increment if start < end
        #we move end up one and decrement if start > end

        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])
        startptr, endptr, answer, counter = 0, 0, 0, 0

        while startptr < len(intervals):
            if starts[startptr] < ends[endptr]:
                counter+=1
                startptr+=1
            else:
                counter-=1
                endptr+=1
            answer = max(answer, counter)
        
        return answer
        
