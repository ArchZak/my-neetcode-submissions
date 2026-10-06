class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #input: array of intervals where values are [start,end]
        #output: merge all overlapping intervals, and return final array

        #array of intervals where values are [start,end]
        #merge all overlapping intervals, and return final array

        #can return answer in any order
        #intervals are nonoverlapping if no common point. so [1,2] and [2,3] overlaps
        
        #constraint:
        #will have at least 1 interval
        #input might not be sorted

        #looping
        #for each interval, we're gonna add them to another list for merges
        #if we detect an overlap, instead of stacking a new array on, we just change the values
        #going to need to sort inputs so we just compare curr start against [-1] merge end

        #1 1 6
        #3 5 7

        #1,5 6,7

        intervals = sorted(intervals, key=lambda x: x[0])

        merges = []
        for interval in intervals:
            if merges and interval[0] <= merges[-1][1]:
                merges[-1][1] = max(merges[-1][1], interval[1])
            else:
                merges.append(interval)

        return merges