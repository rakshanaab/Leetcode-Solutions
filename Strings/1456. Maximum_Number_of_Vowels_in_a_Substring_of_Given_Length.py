# Intuition
We need to find the maximum number of vowels in any substring of length `k`. Instead of counting vowels for every substring separately, we use a sliding window. As the window moves, we remove the leftmost character and add the new rightmost character, updating the vowel count efficiently.

# Approach
1. Define the set of vowels.
2. Count the number of vowels in the first window of size `k`.
3. Store this count as the current maximum.
4. Slide the window one character at a time:
   - If the character leaving the window is a vowel, decrement the count.
   - If the new character entering the window is a vowel, increment the count.
   - Update the maximum vowel count if needed.
5. Return the maximum count.

# Complexity
- Time complexity: **O(n)**
  - We traverse the string only once.

- Space complexity: **O(1)**
  - Only a few variables are used regardless of the input size.

# Code
```python3
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = "aeiou"
        c = max = 0

        for i in range(k):
            if s[i] in vowel:
                c += 1
        max = c

        for i in range(k, len(s)):
            if s[i - k] in vowel:
                c -= 1
            if s[i] in vowel:
                c += 1
            if c > max:
                max = c

        return max
```
