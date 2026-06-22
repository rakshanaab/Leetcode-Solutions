# Intuition
We need to merge two strings by taking characters alternately from each. If one string is longer, the remaining characters are appended at the end. This can be efficiently done using two pointers.

# Approach
1. Initialize two pointers `i` and `j` for `word1` and `word2`.
2. Traverse both strings while at least one pointer is within bounds.
3. If `i` is within `word1`, append `word1[i]` and increment `i`.
4. If `j` is within `word2`, append `word2[j]` and increment `j`.
5. Continue until both strings are fully processed.
6. Join the result list to form the final string.

# Complexity
- Time complexity: **O(n + m)**
  - Each character from both strings is visited exactly once.

- Space complexity: **O(n + m)**
  - A list is used to store the merged result.

# Code
```python3
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        a = []

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                a.append(word1[i])
                i += 1
            if j < len(word2):
                a.append(word2[j])
                j += 1

        return "".join(a)
