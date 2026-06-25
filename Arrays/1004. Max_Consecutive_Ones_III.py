# Intuition
We need to find the longest subarray containing at most `k` zeros, since those zeros can be flipped to `1`s. A sliding window is ideal because it allows us to maintain a valid window while efficiently expanding and shrinking it as needed.

# Approach
1. Initialize two pointers:
   - `l` for the left boundary of the window.
   - `r` for the right boundary of the window.
2. Keep track of the number of zeros in the current window using `z`.
3. Expand the window by moving `r` through the array.
4. If a zero is encountered, increment `z`.
5. If `z` becomes greater than `k`, shrink the window from the left until the number of zeros is at most `k`.
6. After each expansion, update the maximum window length.
7. Return the maximum length found.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python3
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        m = 0
        z = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                z += 1

            while z > k:
                if nums[l] == 0:
                    z -= 1
                l += 1

            m = max(m, r - l + 1)

        return m
```
