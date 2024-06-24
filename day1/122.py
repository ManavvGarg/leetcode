from typing import List


class Solution:
    # 2ptr approach
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # left for buy, right for sell
        l, r = 0, 1
        
        if len(prices) == 0:
            return 0

        while r < len(prices):
            # if left less than right then that means profit
            if prices[l] < prices[r]:
                # calc profit
                profit += (prices[r] - prices[l])
            
            # we move left to right's position as we have to check if stock falls or rises.
            # if rises then profit (again) or loss which in case we dont have to do anything
            l = r
            
            # move right one step ahead
            r += 1
        return profit
        
