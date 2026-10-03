class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            else:
                profit = max(profit, prices[i]-lowest)
        return profit