from collections import deque
from typing import List, Tuple, Set


class Solution:
    def is_valid(self, row, col, row_dim, col_dim)-> bool:
        return 0<=row<row_dim and 0<=col<col_dim

    def bfs(self, grid: List[List[str]], start_node: Tuple[int, int])-> Set[Tuple[int, int]]:
        queue = deque([start_node])
        visited = {start_node}

        while queue:
            current_node = queue.popleft()

            row_current = current_node[0]
            col_current = current_node[1]
            potential_neighbors = [(row_current-1, col_current),
                        (row_current, col_current-1),
                        (row_current+1, col_current),
                        (row_current, col_current+1)]
            neighbors = [(r,c) for r,c in potential_neighbors if self.is_valid(r,c,len(grid), len(grid[0])) and grid[r][c]=="1"]

            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited

    def numIslands(self, grid: List[List[str]]) -> int:
        visited: Set[Tuple[int, int]] = set()
        islands = 0
        for r, row in enumerate(grid):
            for c, item in enumerate(row):
                if (r,c) not in visited and item == "1":
                    result = self.bfs(grid,(r,c))
                    islands += 1
                    visited.update(result)
        return islands

s = Solution()
print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))