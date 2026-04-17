class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #int array of prices where i is price on ith day
        #choose one day to buy, and another day to sell
        #return max profit you can take

        #one pass where you pick lowest price we find, and then use each future day to find max proif

        answer,cheapest = 0, prices[0]
        for price in prices:
            if price < cheapest:
                cheapest = price
            answer = max(answer,price-cheapest)

        return answer