# Intuition
The array contains `n` distinct numbers taken from the range `[0, n]`, with exactly one number missing. Instead of checking each number individually, we can calculate the expected sum of all numbers from `0` to `n` and subtract the actual sum of the array. The difference will be the missing number.

# Approach
1. Find the length of the array, `n`.
2. Calculate the sum of all elements in the array.
3. Compute the expected sum of numbers from `0` to `n` using the formula:
   \[
   \frac{n(n+1)}{2}
   \]
4. Subtract the actual sum from the expected sum.
5. Return the result as the missing number.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python3
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        a = n * (n + 1) // 2
        return a - s
```
