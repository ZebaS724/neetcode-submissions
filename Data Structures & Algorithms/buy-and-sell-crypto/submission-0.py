class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        current_price = prices[0]
        for i in range (len(prices)):
            if prices[i] < current_price:
                current_price = prices[i]
            else:
                current_profit = prices[i] - current_price
                if current_profit > profit:
                    profit = current_profit
        
        return profit
                
        