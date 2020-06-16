class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices)==1:
            return 0
        profit = 0
        for i in range(1,len(prices)):
            profit = max(profit, profit + prices[i]-prices[i-1])
        return profit
