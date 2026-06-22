# Intuition
To maximize the number of content children, we should give the smallest available cookie that can satisfy each child. Sorting both the children's greed factors and the cookie sizes allows us to efficiently match cookies to children using a greedy approach.

# Approach
1. Sort the greed factor array `g` and the cookie size array `s`.
2. Use two pointers:
   - `i` for children.
   - `j` for cookies.
3. Traverse both arrays:
   - If the current cookie can satisfy the current child (`s[j] >= g[i]`), assign the cookie, increment the count, and move to the next child.
   - Regardless of whether the cookie is used, move to the next cookie.
4. Continue until all children or all cookies have been considered.
5. Return the total number of content children.

# Complexity
- Time complexity:
O(n log n + m log m)

- Space complexity:
O(1)

where `n` is the number of children and `m` is the number of cookies.

# Code
```python3
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = 0
        j = 0
        count = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
            j += 1

        return count
```
