# Intuition
Since the array is sorted in ascending order, we can use Binary Search to efficiently find the target element. Instead of checking every element, Binary Search repeatedly divides the search space in half, significantly reducing the number of comparisons.

# Approach
1. Initialize two pointers:
   - `low` at the beginning of the array.
   - `high` at the end of the array.
2. While `low` is less than or equal to `high`:
   - Calculate the middle index `mid`.
   - If `nums[mid]` equals the target, return `mid`.
   - If `nums[mid]` is greater than the target, search the left half by updating `high`.
   - Otherwise, search the right half by updating `low`.
3. If the target is not found after the loop ends, return `-1`.

# Complexity
- Time complexity:
O(log n)

- Space complexity:
O(1)

# Code
```python3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = 0
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1
```
