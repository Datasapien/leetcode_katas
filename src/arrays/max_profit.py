# https://algomaster.io/practice/dsa-patterns
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list

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

# 149 ms, beats 7%
# 19 MB, beats 16%

def xmax_profit(prices):

    if not prices or len(prices) < 2:
        return 0

    # initialised to infinity to ensure any price in list is smaller
    min_price = float('inf')
    max_profit = 0

    for price in prices:

        min_price = min(min_price, price)

        profit = price - min_price

        max_profit = max(max_profit, profit)

    return max_profit

# Kadane's algorithm
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/4868897/most-optimized-kadane-s-algorithm-java-c-python-rust-javascript
# 50 ms, beats 74%
# 20 MB, beats 6%

def max_profit(prices):

    if not prices or len(prices) < 2:
        return 0

    buy = prices[0]
    profit = 0

    for i in range(1, len(prices)):

        if prices[i] < buy:
            buy = prices[i]

        if (prices[i] - buy) > profit:
            profit = prices[i] - buy

    return profit