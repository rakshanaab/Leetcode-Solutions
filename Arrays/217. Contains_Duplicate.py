# Intuition
If an array contains duplicate elements, converting it to a set will remove the repeated values. Therefore, if the size of the set is smaller than the size of the original array, at least one duplicate exists.

# Approach
1. Convert the array `nums` into a set.
2. Compare the length of the set with the length of the original array.
3. If the lengths are different, duplicates are present, so return `True`.
4. Otherwise, all elements are unique, so return `False`.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(n)

# Code
```python3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set(nums)
        if len(a) != len(nums):
            return True
        else:
            return False
