# Intuition
String `t` is formed by shuffling string `s` and adding one extra character. If we sort both strings, their matching characters will line up in the same positions. The first mismatch reveals the extra character.

# Approach
1. Sort both strings `s` and `t`.
2. Compare the characters at each index of `s` and `t`.
3. If a mismatch is found, return the character from `t`.
4. If all characters in `s` match, then the extra character is the last character of the sorted `t`.
5. Return that last character.

# Complexity
- Time complexity: **O(n log n)**
  - Sorting both strings dominates the running time.

- Space complexity: **O(n)**
  - Additional space is used to store the sorted versions of the strings.

# Code
```python3
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)

        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]

        return t[-1]
