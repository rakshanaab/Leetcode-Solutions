# Intuition
Rotating an array to the right by `k` steps means taking the last `k` elements and moving them to the front while shifting the remaining elements to the right. Using Python slicing makes this transformation straightforward.

# Approach
1. Handle cases where `k` is larger than the array length by taking `k % len(nums)`.
2. Split the array into two parts:
   - Last `k` elements: `nums[-k:]`
   - First `n-k` elements: `nums[:-k]`
3. Concatenate them in reversed order: last part + first part.
4. Assign the result back to `nums` using slice assignment (`nums[:]`) to modify the array in-place.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(n) (due to temporary slicing)

# Code
```python3
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
```
