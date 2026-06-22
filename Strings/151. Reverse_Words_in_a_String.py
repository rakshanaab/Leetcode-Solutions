# Intuition
The goal is to reverse the order of words in a string while ignoring extra spaces. Splitting the string naturally breaks it into words, so reversing their order gives the desired result.

# Approach
1. Use `split()` to divide the string into words. This automatically removes extra spaces.
2. Reverse the list of words using `reverse()`.
3. Join the reversed list using a single space to form the final string.

# Complexity
- Time complexity: **O(n)**
  - Splitting, reversing, and joining all take linear time in terms of the length of the string.

- Space complexity: **O(n)**
  - A list is created to store all words.

# Code
```python3
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()      
        words.reverse()        
        return " ".join(words)
