class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer=0
        cheapest=prices[0]

        for i in range(1,len(prices)):
            if prices[i] < cheapest:
                cheapest=prices[i]
            answer=max(answer,prices[i]-cheapest)
            
        return answer