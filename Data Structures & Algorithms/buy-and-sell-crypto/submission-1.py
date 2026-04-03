class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest, profit = prices[0], 0

        for price in prices:
            profit = max(profit,price-cheapest)
            cheapest = min(cheapest,price)
        return profit