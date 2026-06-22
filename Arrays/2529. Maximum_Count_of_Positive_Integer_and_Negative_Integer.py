# Intuition
We need to count how many positive and negative numbers are present in the array. Since zeros are neither positive nor negative, they are ignored. The answer is the larger of the two counts.

# Approach
1. Initialize two counters:
   - `a` for negative numbers.
   - `b` for positive numbers.
2. Traverse the array.
3. If an element is less than `0`, increment `a`.
4. If an element is greater than `0`, increment `b`.
5. Ignore zeros.
6. Return the maximum of `a` and `b`.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python3
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        a = b = 0

        for i in nums:
            if i < 0:
                a += 1
            elif i > 0:
                b += 1

        if b < a:
            return a
        else:
            return b
```
