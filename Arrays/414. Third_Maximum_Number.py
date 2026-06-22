# Intuition
To find the third distinct maximum number, duplicate values should not be counted multiple times. By removing duplicates and sorting the remaining numbers, we can easily access the third largest distinct element. If fewer than three distinct numbers exist, we return the maximum number.

# Approach
1. Convert the array to a set to remove duplicate values.
2. Convert the set back to a list.
3. Sort the list in ascending order.
4. If there are at least three distinct numbers, return the third largest element (`nums[-3]`).
5. Otherwise, return the largest element (`nums[-1]`).

# Complexity
- Time complexity:
O(n log n)

- Space complexity:
O(n)

# Code
```python3
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()

        if len(nums) >= 3:
            return nums[-3]
        else:
            return nums[-1]
```
