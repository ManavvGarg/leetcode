from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2ptr approach for optimal solution
        # left and right init for index 0, and index 1. 
        # left = buy and right = sell
        l, r = 0, 1

        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r # we shift l to r, because as we know that at 'l' we have to buy the stock, l should be the least value to occur. So if we found r to be lower than l, we shift l to r which will become the new minimum

            # we have to update r regardless at each step
            r += 1
        return maxProfit
        