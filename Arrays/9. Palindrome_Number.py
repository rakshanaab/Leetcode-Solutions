# Intuition
A number is a palindrome if it reads the same forward and backward. Converting the number into a string makes it easy to compare it with its reversed version.

# Approach
1. Convert the integer `x` into a string.
2. Reverse the string using slicing `[::-1]`.
3. Compare the original string with the reversed string.
4. If both are equal, return `True`, otherwise return `False`.

# Complexity
- Time complexity:
O(n), where n is the number of digits in the integer (due to string reversal)

- Space complexity:
O(n), because we store the string representation of the number and its reverse

# Code
```python3 []
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        b = a[::-1]
        return a == b
