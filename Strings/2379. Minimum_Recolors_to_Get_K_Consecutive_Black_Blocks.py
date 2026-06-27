# Intuition
To obtain `k` consecutive black blocks, we need to recolor all white blocks within a window of size `k`. Therefore, the minimum number of recolors is simply the minimum number of white blocks present in any window of length `k`.

# Approach
1. Count the number of white blocks (`'W'`) in the first window of size `k`.
2. Store this count as the current minimum.
3. Slide the window one position at a time:
   - If the character leaving the window is `'W'`, decrement the count.
   - If the new character entering the window is `'W'`, increment the count.
   - Update the minimum count.
4. Return the minimum number of white blocks found, which is the minimum recolors required.

# Complexity
- Time complexity: **O(n)**
  - We traverse the string once using a sliding window.

- Space complexity: **O(1)**
  - Only a few variables are used.

# Code
```python3
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        a = 0

        for i in range(k):
            if blocks[i] == 'W':
                a += 1

        c = a

        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                a -= 1
            if blocks[i] == 'W':
                a += 1
            c = min(c, a)

        return c
```
