# Intuition
The majority element appears more than `n / 2` times in the array. After sorting the array, the majority element must occupy the middle position because it appears in more than half of the indices.

# Approach
1. Sort the array in non-decreasing order.
2. Find the middle index using `len(nums) // 2`.
3. Return the element at the middle index.
4. Since the majority element appears more than half the time, it is guaranteed to be at the middle position after sorting.

# Complexity
- Time complexity:
O(n log n)

- Space complexity:
O(1) or O(log n), depending on the sorting implementation.

# Code
```python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        t = len(nums) // 2
        return nums[t]
```
