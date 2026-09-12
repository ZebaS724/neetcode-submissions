class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    current_price = prices[j] - prices[i]

                    max_profit = max(max_profit,current_price)

        return max_profit

        