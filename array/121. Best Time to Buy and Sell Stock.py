class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float('inf')
        max_profit=0
        for price in prices:
            if price < min_price:
                min_price=price
            current_profit=price-min_price
            max_profit=max(max_profit,current_profit)
        return max_profit
        #logic: we need to find the minimum price and maximum profit, so we can iterate through the prices and keep track of the minimum price and maximum profit. If the current price is less than the minimum price, we update the minimum price. We then calculate the current profit by subtracting the minimum price from the current price and update the maximum profit if the current profit is greater than the maximum profit. Finally, we return the maximum profit.
        #time complexity: O(n) where n is the length of the prices array. We are iterating through the prices array once.
        #space complexity: O(1) as we are using only a constant amount of extra space.