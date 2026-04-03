class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = prices[0]
        profit = 0

        for i in range(1,len(prices)):
            if left > prices[i]:
                left = prices[i]
            if profit < prices[i]-left:
                profit = prices[i]-left
        
        return profit if profit > 0 else 0