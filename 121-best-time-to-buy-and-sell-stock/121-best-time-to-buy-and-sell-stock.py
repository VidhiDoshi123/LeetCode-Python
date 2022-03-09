class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_right = prices[0]
        max_profit = 0 
        n = len(prices)
        for i in range(n):
            min_right = min(min_right,prices[i])
            max_profit = max(max_profit, prices[i] - min_right)
        return max_profit