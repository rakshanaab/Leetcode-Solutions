# Intuition
We need to find the longest contiguous subarray that contains at most two distinct fruit types. A sliding window with a dictionary allows us to keep track of the fruit types in the current window and adjust the window whenever more than two types are present.

# Approach
1. Initialize:
   - A dictionary `d` to store the count of each fruit type in the current window.
   - A left pointer `l` and a variable `m` to store the maximum window size.
2. Expand the window by moving the right pointer `r`.
3. Add the current fruit to the dictionary or increase its count.
4. If the window contains more than two distinct fruit types:
   - Shrink the window from the left.
   - Decrease the count of the leftmost fruit.
   - Remove it from the dictionary if its count becomes zero.
5. After each valid window, update the maximum window length.
6. Return the maximum number of fruits collected.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

(The dictionary stores at most 3 fruit types at any time, so the extra space is constant.)

# Code
```python3
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        m = 0
        l = 0

        for r in range(len(fruits)):
            if fruits[r] in d:
                d[fruits[r]] += 1
            else:
                d[fruits[r]] = 1

            while len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l += 1

            m = max(m, r - l + 1)

        return m
```
