from typing import List, Set


class Solution:
    def DFS(self, adj_list: List[List[int]], node: int, visited: Set[int]):
        visited.add(node)

        for n in adj_list[node]:
            if n not in visited:
                self.DFS(adj_list, n, visited)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adj_list: List[List[int]] = [[] for _ in range(len(rooms))]
        for idx, keys in enumerate(rooms):
            adj_list[idx].extend(keys)
        visited = set()
        self.DFS(adj_list, 0, visited)
        return len(visited) == len(rooms)

if __name__ == "__main__":
    s = Solution()
    print(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))