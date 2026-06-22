# Intuition
Two strings are anagrams if they contain the same characters with the same frequencies. Since anagrams must have equal lengths, we first check the lengths. Then, for each unique character in `s`, we compare its frequency in both strings.

# Approach
1. Check if the lengths of `s` and `t` are equal.
   - If not, return `False` immediately.
2. Create a set of unique characters from `s`.
3. For each character in the set:
   - Count its occurrences in `s` and `t`.
   - If the counts differ, return `False`.
4. If all character frequencies match, return `True`.

# Complexity
- Time complexity: **O(n²)**
  - The `count()` method takes **O(n)** time, and it is called for each unique character.

- Space complexity: **O(k)**
  - Where `k` is the number of unique characters in `s`, due to the set.

# Code
```python3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        st = set(s)

        for i in st:
            if s.count(i) != t.count(i):
                return False

        return True
