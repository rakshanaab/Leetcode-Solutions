# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        a=[0]*n
        if k==0:
            return a
        elif k>0:
            s=sum(code[1:k+1])
            for i in range(n):
                a[i]=s
                s=s-code[(i+1)%n]+code[(i+k+1)%n]
        else:
            k=-k
            s=sum(code[n-k:n])
            for i in range(n):
                a[i]=s
                s=s-code[(i-k)%n]+code[i]
        return a
```
