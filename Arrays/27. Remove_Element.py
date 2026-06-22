# Intuition
We need to remove all occurrences of a given value `val` from the array in-place. Instead of creating a new array, we can overwrite the unwanted elements by shifting valid elements forward.

# Approach
1. Use a pointer `k` to track the position where the next valid element should be placed.
2. Traverse the array using index `i`.
3. If `nums[i]` is not equal to `val`, copy it to `nums[k]` and increment `k`.
4. Continue until the end of the array.
5. Return `k`, which represents the new length of the modified array.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python3
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
```
