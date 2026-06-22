# Intuition
We need to find the longest sequence of consecutive `1`s in the array. As we traverse the array, we can keep track of the current streak of `1`s and update the maximum streak found so far.

# Approach
1. Initialize two variables:
   - `c` to count the current consecutive `1`s.
   - `ans` to store the maximum consecutive `1`s found.
2. Traverse the array.
3. If the current element is `1`:
   - Increment `c`.
   - Update `ans` with the maximum of `ans` and `c`.
4. If the current element is `0`:
   - Reset `c` to `0` since the streak is broken.
5. Return `ans` after processing all elements.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python3
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        ans = 0

        for i in nums:
            if i == 1:
                c += 1
                ans = max(ans, c)
            else:
                c = 0

        return ans
```
