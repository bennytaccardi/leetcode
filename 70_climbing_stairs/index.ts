function climbStairs(n: number): number {
  const tab: number[] = Array(n + 1).fill(-1);
  if (n >= 0) tab[0] = 1;
  if (n >= 1) tab[1] = 1;
  for (let i = 2; i <= n; i++) {
    tab[i] = tab[i - 1] + tab[i - 2];
  }
  return tab[n];
}
