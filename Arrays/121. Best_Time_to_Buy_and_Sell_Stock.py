# Intuition
To maximize profit, we need to buy at the lowest price before selling at a higher price. While traversing the array, we keep track of the minimum price seen so far and calculate the profit that could be made by selling on the current day. The maximum such profit is the answer.

# Approach
1. Initialize `min` with the first stock price.
2. Initialize `mp` (maximum profit) as `0`.
3. Traverse the prices starting from the second day.
4. For each price:
   - Calculate the profit if the stock were sold on that day.
   - Update the minimum price if a lower price is found.
   - Update the maximum profit if the current profit is greater.
5. Return the maximum profit after processing all prices.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        mp = 0

        for i in range(1, len(prices)):
            p = prices[i] - min

            if prices[i] < min:
                min = prices[i]

            if p > mp:
                mp = p

        return mp
```
