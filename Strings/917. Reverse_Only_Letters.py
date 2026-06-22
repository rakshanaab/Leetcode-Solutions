# Intuition
We need to reverse only the letters in the string while keeping all non-letter characters (like digits or symbols) in their original positions. Using two pointers allows us to swap only valid letters from both ends efficiently.

# Approach
1. Convert the string into a list because strings are immutable.
2. Initialize two pointers:
   - `left` at the start
   - `right` at the end
3. While `left < right`:
   - If both characters are letters (`isalpha()`), swap them and move both pointers inward.
   - If the left character is not a letter, move `left` forward.
   - Otherwise, move `right` backward.
4. Convert the list back into a string and return it.

# Complexity
- Time complexity: **O(n)**
  - Each character is processed at most once.

- Space complexity: **O(n)**
  - A list is created from the string for in-place modification.

# Code
```python3
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s = list(s)

        while left < right:
            if s[left].isalpha() and s[right].isalpha():
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif not s[left].isalpha():
                left += 1
            else:
                right -= 1

        return "".join(s)
