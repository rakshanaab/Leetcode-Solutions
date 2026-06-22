# Intuition
The problem is about finding the maximum water that can be contained between two vertical lines. A brute-force approach checks all pairs, but we can optimize using a two-pointer technique by always moving the pointer with the smaller height to potentially find a larger area.

# Approach
1. Initialize two pointers:
   - `left` at the start of the array.
   - `right` at the end of the array.
2. Compute the area formed between `left` and `right`:
   - Width = `right - left`
   - Height = `min(height[left], height[right])`
3. Update the maximum area found so far.
4. Move the pointer pointing to the smaller height inward:
   - If `height[left] < height[right]`, increment `left`.
   - Else, decrement `right`.
5. Repeat until both pointers meet.
6. Return the maximum area.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python3
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            ans = max(ans, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans
```
