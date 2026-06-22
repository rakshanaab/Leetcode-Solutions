# Intuition
The intersection of two arrays consists of the distinct elements that appear in both arrays. By converting the arrays into sets, duplicate values are removed automatically, and we can use the set intersection operation to find the common elements efficiently.

# Approach
1. Convert `nums1` into a set to keep only unique elements.
2. Convert `nums2` into a set to keep only unique elements.
3. Use the set intersection operator `&` to find elements present in both sets.
4. Convert the resulting set back to a list and return it.

# Complexity
- Time complexity:
O(n + m)

- Space complexity:
O(n + m)

where `n` is the length of `nums1` and `m` is the length of `nums2`.

# Code
```python3
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)
```
