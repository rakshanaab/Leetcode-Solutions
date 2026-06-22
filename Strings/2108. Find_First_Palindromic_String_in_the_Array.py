# Intuition
We need to find the first word in the list that is a palindrome. A word is a palindrome if it reads the same forward and backward. So we can simply check each word one by one and return the first match.

# Approach
1. Iterate through each word in the list.
2. For each word, check if it is equal to its reverse (`word == word[::-1]`).
3. If it is a palindrome, store it and break the loop.
4. If a palindrome was found, return it.
5. Otherwise, return an empty string.

# Complexity
- Time complexity: **O(n · m)**
  - `n` is the number of words and `m` is the average length of a word (for reversal check).

- Space complexity: **O(1)**
  - No extra space is used apart from variables.

# Code
```python3
from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""
