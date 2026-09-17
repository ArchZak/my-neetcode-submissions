"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #input: list of [int,int] not ordered
        #output: can person attend all meetings? (boolean)

        #array of [[starti,endi]] where start < end, can person attend all meetings
        #intervals can be given in any order 

        #array can be empty

        #split intervals into two arrays of start and finish after sorting it
        #then need pointers on start and end array
        #basically just need to find an end bigger than start
        #starting at 0, 0 -> move start up one and if bigger than old end, move end up 1
        #if we come across an instance where end_i-1 < start_i, then we return false

        #interval_sort = [(x.start, x.end) for x in intervals]
        #.sort()
        #start = get start, end = get ends
        #startptr, endptr = 1, 0
        #while start < len start:
        #   if start val < end val:
        #       return false
        #   end++, start++
        #return true

        interval_sort = [(x.start, x.end) for x in intervals]
        interval_sort.sort()

        for i in range(1, len(interval_sort)):
            if interval_sort[i][0] < interval_sort[i-1][1]:
                return False

        return True
        