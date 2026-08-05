"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #input: an array of intervals where start_i < end_i
        #output: find minimum number of rooms to schedule all meetings without conflict

        #start_i == end_i is not a conflict
        #so while the start pointer is less than the len of the array
        #move the two pointers through the arrays
        #if curr start is less than curr end, move it up, increase rooms
        #if curr end is bigger than curr start, decrement count, take max all the time
        

        starts = sorted([inter.start for inter in intervals])
        ends = sorted([inter.end for inter in intervals])
        i, j, answer, temp = 0, 0, 0, 0
        while i < len(starts):
            if starts[i] < ends[j]:
                temp+=1
                i+=1
            else:
                temp-=1
                j+=1

            answer = max(answer,temp)

        return answer
