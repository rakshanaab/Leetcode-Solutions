# Intuition
Since the array can contain negative numbers, squaring them may change their order. However, once squared, all values become non-negative, so we can compute all squares first and then sort them to get the final result.

# Approach
1. Create an empty list `a` to store squared values.
2. Traverse each element in `nums`.
3. Square each element and append it to `a`.
4. Sort the resulting list.
5. Return the sorted squared array.

# Complexity
- Time complexity:
O(n log n) (due to sorting)

- Space complexity:
O(n)

# Code
```python3
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = []

        for i in range(len(nums)):
            a.append(nums[i] * nums[i])

        return sorted(a)
```
