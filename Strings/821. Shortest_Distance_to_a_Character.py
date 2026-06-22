# Intuition
For each position in the string, we need to find the shortest distance to the given character `c`. A direct idea is to check every position and compute its distance to all occurrences of `c`, then take the minimum.

# Approach
1. Iterate through each index `i` in the string.
2. For each `i`, initialize a variable `m` as infinity.
3. Traverse the entire string again using index `j`.
4. If `s[j] == c`, compute the distance `abs(i - j)` and update the minimum distance.
5. Store the minimum distance for each index in a result list.
6. Return the final list.

# Complexity
- Time complexity: **O(n²)**
  - For each character, we scan the entire string again.

- Space complexity: **O(n)**
  - We store the result list of size `n`.

# Code
```python3
from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        a = []

        for i in range(n):
            m = float('inf')
            for j in range(n):
                if s[j] == c:
                    m = min(m, abs(i - j))
            a.append(m)

        return a
