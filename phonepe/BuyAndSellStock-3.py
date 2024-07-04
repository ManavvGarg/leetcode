from typing import List

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.



Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.



Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # follow the approach of buying and selling the stock two times on the same day. At MOST 2 transactions
        # a transaction is: buy and sell

        # check if the price list exists (edge case)
        if not prices:
            return 0
        
        # init variables
        # we are going to have 4 VARs.
        # First Buy, First Sell
        # Second Buy, Second Sell
        firstBuy = -prices[0] # as this is the first transaction, we dont ahve any profit so we pay out of own pocket
        firstSell = float('-inf') # we dont know when we are gonna sell right now without traversing the array so init with -ve inf
        secondBuy = float('-inf') # we dont know when we are gonna buy the second time right now without traversing the array so init with -ve inf
        secondSell = float('-inf') # we dont know when we are gonna sell the second time right now without traversing the array so init with -ve inf


        # we are going to solve this problem with the help of state transitions. We have 4 states in total, i.e, the 4 variables we set earlier
        # We can buy, sell, secondBuy, secondSell
        
        for price in prices:
            # we can either stay on the same state, or buy the stock. If we buy then profit goes down as we are not selling rn, so -price
            firstBuy = max(firstBuy, -price)
            # we can either hold the stock (stay in the same state) or sell the stock which we bought earlier (firstBuy)
            firstSell = max(firstSell, firstBuy+price) # selling price added to the spend amount will tell us the actual profit
            # we can either stay on the same state ( not buying ), or buy the stock
            secondBuy = max(secondBuy, firstSell-price) # going from selling state to buying state so profit made from selling - price will return profit after buying 
            # we can either stay on the same state (holding) or sell the stock which we bought earlier (secondBuy)
            secondSell = max(secondSell, secondBuy+price)

        return secondSell # secondSell is the last state and it will carry the max profit 

        