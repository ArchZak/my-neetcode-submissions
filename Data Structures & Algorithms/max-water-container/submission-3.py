class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #inputs: an array of integers where i is height there
        #output: area to form a container and return max amount of water

        left, right = 0, len(heights)-1
        answer = 0
        while left < right:
            answer = max(answer, min(heights[left], heights[right])*(right-left))
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        
        return answer