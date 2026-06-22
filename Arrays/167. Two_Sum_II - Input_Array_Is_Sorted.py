# Intuition
Since the array is sorted, we can efficiently find the two numbers using the two-pointer technique. By placing one pointer at the start and another at the end, we can adjust them based on whether the current sum is too small or too large.

# Approach
1. Initialize two pointers:
   - `left` at the beginning of the array.
   - `right` at the end of the array.
2. Compute the sum of `numbers[left] + numbers[right]`.
3. If the sum equals the target, return the indices (1-based).
4. If the sum is less than the target, move `left` forward to increase the sum.
5. If the sum is greater than the target, move `right` backward to decrease the sum.
6. Continue until the correct pair is found.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python3
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1
```
