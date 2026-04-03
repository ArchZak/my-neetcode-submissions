class Solution:
    def maxArea(self, heights: List[int]) -> int:
        answer=0
        left,right=0,len(heights)-1

        while left < right:
            temp=min(heights[left]*(right-left),heights[right]*(right-left))
            answer=max(answer,temp)
            if heights[right] < heights[left]:
                right-=1
            else:
                left+=1

        return answer