class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(0, len(prices)):
            for j in range(i, len(prices)):
                res = max(prices[j] - prices[i], res)
        return res