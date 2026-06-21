# Intuition
To determine whether a string is a palindrome, we only need to compare its characters from both ends. Since the problem ignores non-alphanumeric characters and is case-insensitive, we first create a cleaned version of the string containing only lowercase letters and digits. Then, we check if the cleaned string reads the same forwards and backwards.

# Approach
1. Traverse the input string.
2. Keep only alphanumeric characters using `isalnum()`.
3. Convert each valid character to lowercase and store it in a list.
4. Compare the list with its reversed version.
5. If both are equal, the string is a palindrome; otherwise, it is not.

# Complexity
- Time complexity: **O(n)**
  - We iterate through the string once and reverse the cleaned list once.

- Space complexity: **O(n)**
  - An additional list is used to store the filtered characters.

# Code
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        for i in range(len(s)):
            if s[i].isalnum():
                a.append(s[i].lower())

        return a == a[::-1]
