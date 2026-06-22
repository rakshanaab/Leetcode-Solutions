# Intuition
Every element in the array appears twice except for one element that appears only once. Using the XOR (`^`) operation, identical numbers cancel each other out because `x ^ x = 0`, and `x ^ 0 = x`. Therefore, XORing all elements together leaves only the unique element.

# Approach
1. Initialize a variable `a` to `0`.
2. Traverse the array and XOR each element with `a`.
3. Pairs of identical numbers cancel each other out.
4. After processing all elements, `a` will contain the number that appears only once.
5. Return `a`.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python3
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
```
