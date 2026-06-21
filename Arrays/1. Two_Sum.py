# Intuition
A brute-force approach is sufficient because we can check every possible pair of numbers in the array. If the sum of any pair equals the target, we return their indices immediately.

# Approach
Use two nested loops:
1. Fix the first element using index `i`.
2. Check every element after it using index `j`.
3. If `nums[i] + nums[j] == target`, return the indices `(i, j)`.

Since every pair is examined once, the correct answer is guaranteed to be found.

# Complexity
- Time complexity:
O(n²)

- Space complexity:
O(1)

# Code
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
