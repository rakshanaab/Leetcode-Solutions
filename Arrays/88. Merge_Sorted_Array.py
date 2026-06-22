# Intuition
Since both arrays are already sorted, we can merge them efficiently from the end. Starting from the last valid elements of `nums1` and `nums2`, we place the larger element at the end of `nums1`. This avoids overwriting elements in `nums1` that have not yet been processed.

# Approach
1. Initialize three pointers:
   - `i = m - 1` pointing to the last valid element in `nums1`.
   - `j = n - 1` pointing to the last element in `nums2`.
   - `k = m + n - 1` pointing to the last position in `nums1`.
2. Compare `nums1[i]` and `nums2[j]`.
3. Place the larger element at `nums1[k]` and move the corresponding pointer backward.
4. Continue until either array is exhausted.
5. If elements remain in `nums2`, copy them into `nums1`.
6. No extra work is needed for remaining elements in `nums1` since they are already in the correct position.

# Complexity
- Time complexity:
O(m + n)

- Space complexity:
O(1)

# Code
```python3
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
```
