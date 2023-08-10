class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=0
        profit=0
        for sell in range(1, len(prices)):
            if prices[buy]>prices[sell]:
                buy=sell
            if prices[sell]-prices[buy]>profit:
                profit=prices[sell]-prices[buy]
        return (profit)