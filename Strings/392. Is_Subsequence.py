# Intuition
A subsequence means the characters of `s` must appear in `t` in the same order, but not necessarily consecutively. So we can scan through `t` and try to match characters of `s` one by one in order.

# Approach
1. Use a pointer `i` to track the current index in string `s`.
2. Traverse each character in string `t`.
3. If the current character in `t` matches `s[i]`, move `i` forward.
4. Continue until the end of `t`.
5. If `i` reaches the length of `s`, it means all characters were matched in order, so `s` is a subsequence of `t`.

# Complexity
- Time complexity: **O(n)**
  - We traverse string `t` once.

- Space complexity: **O(1)**
  - Only a single pointer is used, no extra space depends on input size.

# Code
```python3
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for a in t:
            if i < len(s) and s[i] == a:
                i += 1
        return len(s) == i
