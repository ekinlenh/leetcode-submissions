class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we want to keep track of a min price as we traverse
        # because having a min price means a better profit
        # so make min_price = prices[0]
        # go through rest of the list
        # if prices[i] < min_price, we have a better price to buy at
        # else, we can sell for a profit at that day
        # and we keep track of the max profit we get

        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_price: # new buy day
                min_price = prices[i]
            else: # sell day 
                max_profit = max(max_profit, prices[i] - min_price)
        
        return max_profit
