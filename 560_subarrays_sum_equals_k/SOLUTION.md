# Title

560 Subarrays sum equals k -> O(n) solution in typescript

# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

# Approach

Prefix sum array using an hash map

# Complexity

- Time complexity:
  $$O(n)$$

- Space complexity:
  $$O(n)$$

# Code

```
function subarraySum(nums: number[], k: number): number {
  let p = 0;
  let a = 0;
  const counter = new Map();
  counter.set(0, 1);
  for (const num of nums) {
    p += num;
    const retrievedValue = counter.get(p - k) ?? 0;
    a += retrievedValue ?? 0;
    if (counter.has(p)) {
      const existingRetrievedValue = counter.get(p);
      counter.set(p, existingRetrievedValue + 1);
    } else {
      counter.set(p, 1);
    }
  }
  return a;
}
```
