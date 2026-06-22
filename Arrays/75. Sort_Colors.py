# Intuition
This problem is about sorting an array containing only three distinct values (0, 1, and 2). Instead of using a general sorting algorithm, we can use the Dutch National Flag algorithm, which sorts the array in a single pass using three pointers.

# Approach
1. Initialize three pointers:
   - `low` to track the position for 0s.
   - `mid` to traverse the array.
   - `high` to track the position for 2s.
2. Traverse the array while `mid <= high`:
   - If `nums[mid] == 0`, swap it with `nums[low]`, and move both `low` and `mid` forward.
   - If `nums[mid] == 1`, just move `mid` forward.
   - If `nums[mid] == 2`, swap it with `nums[high]` and move `high` backward.
3. Continue until all elements are correctly placed.
4. The array will be sorted in-place.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python3
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```
