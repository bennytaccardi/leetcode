function subarraySum(nums: number[], k: number): number {
  let p = 0;
  let a = 0;
  const counter = new Map();
  counter.set(0, 1);
  for (const num of nums) {
    console.log(counter);
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

const result = subarraySum([1, 1, 1], 2);
console.log(result);
