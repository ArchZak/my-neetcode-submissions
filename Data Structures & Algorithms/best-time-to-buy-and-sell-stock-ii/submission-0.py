class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #input: list of prices 
        #output: max profit achieved

        #given list of prices of stock on ith day
        #you may decide to buy or sell stock
        #you can buy and then sell stock on same day tho
        #can do any number of transaction but can only buy 1 share at a time

        #append 0 to end of array
        #going to buy if stock costs more tmr 
        #going to sell if stock costs less tmr 

        answer = 0
        prices.append(0)
        have_stock = False

        for i in range(len(prices)-1):
            if not have_stock and prices[i] < prices[i+1]:
                answer-=prices[i]
                have_stock = True
            elif have_stock and prices[i] > prices[i+1]:
                answer+=prices[i]
                have_stock = False

        return answer