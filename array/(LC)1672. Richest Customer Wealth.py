class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth=float('-inf')
        for wealth in accounts:
            max_wealth=max(max_wealth,sum(wealth))
        return max_wealth

#Logic:we need to find the maximum wealth among all the customers. We iterate through each customer's wealth and calculate the sum of their wealth. We maintain a variable max_wealth to store the maximum wealth found so far and update it if the current sum is greater than max_wealth. Finally, we return max_wealth.
#Time Complexity: O(m*n) where m is the number of customers and n is the number of accounts per customer.
#Space Complexity: O(1) since we are not using any extra space, we are just using a counter to count the number of words with the given prefix.