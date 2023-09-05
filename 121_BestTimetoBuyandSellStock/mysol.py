'''
To find the best time to sell a stock to solve the problem, follow this approach:
1. Initialize two pointers: a "buy" pointer, indicating the day to buy the stock, and a "sell" pointer, representing the day to sell the stock.
2. Initialize a "profit" variable to 0, which will track the maximum profit.
3. Iterate through the array with the "sell" pointer:
If the price at the "sell" pointer is less than the price at the "buy" pointer, update the "buy" pointer to the "sell" pointer. This ensures that you consider buying at a potentially lower price.
Calculate the current profit as the price at the "sell" pointer minus the price at the "buy" pointer.
4. Update the maximum profit whenever the current profit is greater than the previous maximum profit.
5. After iterating through the entire array, return the "profit" variable, which holds the maximum profit achievable with this strategy.
This approach effectively finds the optimal time to buy and sell the stock to maximize profit while considering the sliding window of potential buying opportunities.
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=0 # Set the buy pointer to the start of the prices array
        profit=0 # Set max profit to 0
        for sell in range(1, len(prices)): # Iterate through the array with the sell pointer
            if prices[buy]>prices[sell]: # If the price at the sell pointer is less than the price at the buy pointer
                buy=sell # Update the buy pointer to the sell pointer
            if prices[sell]-prices[buy]>profit: # If current profit is greater than max profit
                profit=prices[sell]-prices[buy] # Update max profit 
        return (profit) # Return the max profit