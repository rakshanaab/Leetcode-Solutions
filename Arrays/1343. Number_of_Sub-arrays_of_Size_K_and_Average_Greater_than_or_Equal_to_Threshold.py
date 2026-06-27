# Intuition
We need to count the number of subarrays of size `k` whose average is greater than or equal to the given threshold. Instead of calculating the sum of every subarray from scratch, we can use a sliding window to update the sum efficiently as the window moves.

# Approach
1. Calculate the sum of the first `k` elements.
2. Compute the average of the first window and increment the count if it meets the threshold.
3. Slide the window one element at a time:
   - Remove the element leaving the window.
   - Add the new element entering the window.
   - Compute the average of the current window.
   - If the average is greater than or equal to the threshold, increment the count.
4. Return the total count of valid subarrays.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python3
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum = 0
        m = c = 0

        for i in range(k):
            sum += arr[i]

        m = sum // k
        if m >= threshold:
            c += 1

        for i in range(k, len(arr)):
            v = arr[i - k]
            sum = sum - v
            sum += arr[i]

            m = sum // k
            if m >= threshold:
                c += 1

        return c
```

