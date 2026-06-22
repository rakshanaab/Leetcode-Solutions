# Intuition
To reverse only the vowels in a string, we can use two pointers: one starting from the beginning and the other from the end. We move the pointers until they both point to vowels, then swap them. This process continues until the pointers meet, ensuring that only vowels are reversed while all other characters remain in their original positions.

# Approach
1. Convert the string into a list since strings are immutable in Python.
2. Initialize two pointers:
   - `left` at the start of the list.
   - `right` at the end of the list.
3. While `left < right`:
   - If both characters are vowels, swap them and move both pointers inward.
   - If the left character is not a vowel, move `left` forward.
   - If the right character is not a vowel, move `right` backward.
4. Convert the modified list back into a string and return it.

# Complexity
- Time complexity: **O(n)**
  - Each character is visited at most once by either pointer.

- Space complexity: **O(n)**
  - The string is converted into a list to allow in-place modifications.

# Code
```python3
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] in 'AEIOUaeiou' and s[right] in 'AEIOUaeiou':
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] not in 'AEIOUaeiou':
                left += 1
            elif s[right] not in 'AEIOUaeiou':
                right -= 1

        return "".join(s)
