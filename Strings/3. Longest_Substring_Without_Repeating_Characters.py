# Intuition
To find the longest substring without repeating characters, we use a sliding window. We expand the window by moving the right pointer and keep track of the characters currently in the window using a set. If a duplicate character is encountered, we shrink the window from the left until the duplicate is removed.

# Approach
1. Initialize two pointers:
   - `l` as the left boundary of the sliding window.
   - `r` as the right boundary while traversing the string.
2. Use a set `seen` to store the unique characters in the current window.
3. For each character at index `r`:
   - While the character is already in `seen`, remove characters from the left of the window and move `l` forward.
   - Add the current character to `seen`.
   - Update the maximum window length.
4. Return the maximum length found.

# Complexity
- Time complexity: **O(n)**
  - Each character is added to and removed from the set at most once.

- Space complexity: **O(min(n, m))**
  - Where `m` is the size of the character set. In the worst case, the set stores all unique characters in the current window.

# Code
```python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        ans = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            ans = max(ans, r - l + 1)

        return ans
```
