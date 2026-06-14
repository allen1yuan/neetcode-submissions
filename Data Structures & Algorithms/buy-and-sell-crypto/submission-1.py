class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1
        # moving window to right
        # l is buy pointer, r is sell
        while r < len(prices):
            # sell at only positive price
            if prices[r] > prices[l]:
                profit = max(prices[r] - prices[l], profit)
            else:
                # there exist a lower price
                # we want buy at lower price
                # make the sell to buy
                l = r
            # check all case of sell price > current buy price
            r += 1
        return profit

