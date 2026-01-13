from typing import List, Set


class Solution:
    def DFS(self, adj_list: List[List[int]], node: int, visited: Set[int], nums: List[int], comb: List[int], total_comb: List[List[int]]):
        visited.add(node)
        comb.append(nums[node])
        if len(comb) == len(nums):
            total_comb.append(comb.copy())
        for n in adj_list[node]:
            if n not in visited:
                self.DFS(adj_list, n, visited, nums, comb, total_comb)
        comb.pop()
        visited.remove(node)
        return total_comb
    def permute(self, nums: List[int]) -> List[List[int]]:
        adj_list: List[List[int]] = []
        for idx, num in enumerate(nums):
            adj_list.append([i for i in range(len(nums)) if i != idx])
        res = []
        for i, n in enumerate(nums):
            partial_res = self.DFS(adj_list, i, set(), nums, [], [])
            for p_r in partial_res:
                res.append(p_r)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.permute(nums = [1,2,3]))