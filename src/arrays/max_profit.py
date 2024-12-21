# https://algomaster.io/practice/dsa-patterns
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0. 

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

# :)

def max_profit(prices):

    max_profit = 0

    if len(prices) == 0 or prices == sorted(prices, reverse=True):
        return max_profit

    index_min = min(range(len(prices)), key=prices.__getitem__)
    index_max = max(range(len(prices)), key=prices.__getitem__)
    
    if index_min < index_max:

        max_profit = prices[index_max] - prices[index_min]

    return max_profit