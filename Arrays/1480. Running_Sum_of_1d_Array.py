# Intuition
The running sum at any index is the sum of all elements from the beginning of the array up to that index. We can keep a cumulative total while traversing the array and store each updated sum in a new list.

# Approach
1. Initialize an empty list `a` to store the running sums.
2. Initialize a variable `sum` to `0`.
3. Traverse the array from left to right.
4. Add the current element to `sum`.
5. Append the updated `sum` to the result list.
6. After processing all elements, return the list containing the running sums.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(n)

# Code
```python3
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a = []
        sum = 0

        for i in range(len(nums)):
            sum = nums[i] + sum
            a.append(sum)

        return a
```
