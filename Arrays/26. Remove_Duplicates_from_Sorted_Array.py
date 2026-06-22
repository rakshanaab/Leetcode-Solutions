# Intuition
Since the array is sorted, all duplicates appear consecutively. We can use a two-pointer technique to keep track of the position of unique elements and overwrite duplicates in-place.

# Approach
1. Initialize a pointer `i` at index `0`, which tracks the position of the last unique element.
2. Traverse the array using another pointer `j` starting from index `1`.
3. If `nums[j]` is different from `nums[i]`, it means we found a new unique element:
   - Increment `i`.
   - Copy `nums[j]` to `nums[i]`.
4. Continue this process until the end of the array.
5. Return `i + 1`, which is the count of unique elements.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
```
