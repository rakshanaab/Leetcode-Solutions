# Intuition
The wealth of a customer is the sum of all the money they have across their bank accounts. To find the richest customer, calculate the wealth of each customer and return the maximum wealth among them.

# Approach
1. Create an empty list `b` to store the wealth of each customer.
2. Traverse through the `accounts` array.
3. For each customer, calculate the sum of their accounts using `sum()`.
4. Append the calculated wealth to `b`.
5. Return the maximum value from `b`, which represents the richest customer's wealth.

# Complexity
- Time complexity:
O(m × n), where `m` is the number of customers and `n` is the average number of accounts per customer.

- Space complexity:
O(m), due to the additional list used to store each customer's wealth.

# Code
```python3
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        b = []
        for i in range(len(accounts)):
            b.append(sum(accounts[i]))
        return max(b)
```
