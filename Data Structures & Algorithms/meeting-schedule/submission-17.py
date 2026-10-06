"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #input: array of ints where [start,end] and start<end
        #output: can person make all meetings

        #array of meeting times with [start,end] where start < end
        #bool if person can make it to all the meetings
        #end_1 and start_2 being the same isnt an overlap

        #constraints:
        #array might not be sorted on input
        #may have 0 meetings actually

        #sort
        #going to start array by starts and then loop through array
        #if a start and an end overlap then return false, if exit return true

        # new_intervals = sorted([[x.start, x.end] for x in intervals], key=lambda x: x[0])
        intervals = sorted(intervals, key=lambda x: x.start)
        
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False

        return True