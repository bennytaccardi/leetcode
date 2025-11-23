from collections import deque
from typing import List, Tuple


class Solution:
    @staticmethod
    def is_valid(row, col, row_dim, col_dim)-> bool:
        return 0<=row<row_dim and 0<=col<col_dim
    @staticmethod
    def get_all_starting_nodes(_grid: List[List[int]]) -> List[Tuple[int, int]]:
        return [(r,c) for r, row in enumerate(_grid) for c, col in enumerate(row) if _grid[r][c] == 2 ]

    def _bfs(self, _grid: List[List[int]]):
        starting_nodes = Solution.get_all_starting_nodes(_grid)
        visited = set()
        queue = deque([])
        for starting_node in starting_nodes:
            visited.add(starting_node)
            queue.append({"level": 0, "node": starting_node})
        step = 0
        while queue:
            current_item = queue.popleft()
            current_node = current_item["node"]
            current_level = current_item["level"]
            step = current_level
            current_row, current_col = current_node
            potential_neighbors = [
                (current_row-1, current_col),
                (current_row+1, current_col),
                (current_row, current_col-1),
                (current_row, current_col+1),
            ]
            neighbors = [(r,c) for r,c in potential_neighbors if Solution.is_valid(r, c, len(_grid), len(_grid[0])) and _grid[r][c] == 1]

            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append({"level": current_level + 1, "node": neighbor})
                    _grid[neighbor[0]][neighbor[1]] = 2
        any_healty = any([True if item == 1 else False for row in _grid for item in row])
        return step if not any_healty else -1
    def orangesRotting(self, grid: List[List[int]]) -> int:
        all_healthy = all(item == 1 for r in grid for item in r)
        all_empty = all(item == 0 for r in grid for item in r)
        if all_healthy:
            return -1
        if all_empty:
            return 0
        return self._bfs(grid)

s = Solution()
res = s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
print(res)
