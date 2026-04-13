class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #input: array of intervals where intervals[i] is [starti, endi]
        #output: array of nonoverlapping intervals that cover all intervals in input

        #order doesnt matter
        #merge all overlapping intervals and return remaining array
        
        #need to sort array cause otw it's awko solve if possible
        #loop through the array and compare end of i-1 to start of i
        #if end i-1 >= start i then take min of start and max of end
        #have a while loop with sentinel saying if we changed something in the curr for loop

        sentinel = True

        while sentinel:
            sentinel = False
            intervals.sort()
            for i in range(1,len(intervals)):
                if intervals[i-1][1] >= intervals[i][0]:
                    sentinel = True
                    new_entry = [min(intervals[i-1][0], intervals[i][0]), max(intervals[i-1][1], intervals[i][1])]
                    intervals.pop(i)
                    intervals.pop(i-1)
                    intervals.insert(1, new_entry)
                    break
                    
        return intervals
