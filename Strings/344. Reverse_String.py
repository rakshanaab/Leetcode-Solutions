# Intuition
To reverse the character array in-place, we can swap the first and last characters, then move inward and continue swapping until we reach the middle of the array. This avoids using extra space and satisfies the in-place requirement.

# Approach
1. Initialize two pointers:
   - `low` at the beginning of the array.
   - `high` at the end of the array.
2. Calculate the midpoint of the array.
3. While `low` is before the midpoint:
   - Swap the characters at `low` and `high`.
   - Increment `low`.
   - Decrement `high`.
4. After all swaps, the array is reversed in-place.

# Complexity
- Time complexity: **O(n)**
  - Each element is swapped at most once.

- Space complexity: **O(1)**
  - No extra space is used apart from a few variables.

# Code
```python3
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        a = len(s) // 2
        low = 0
        high = len(s) - 1

        while low < a:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
