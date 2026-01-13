from typing import List, Set


class Solution:
    def DFS(self, node: int, adj_list: List[List[int]], visited: List[int]):
        if visited[node] == 1:
            return True
        if visited[node] == 2:
            return False
        visited[node] = 1
        for n in adj_list[node]:
            if self.DFS(n, adj_list, visited):
                return True
        visited[node] = 2
        return False
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        for i in range(numCourses):
            adj_list[i] = []
        for exam, pre in prerequisites:
            adj_list[exam].append(pre)
        state = [0] * numCourses
        for i in range(numCourses):
            if state[i]:
                if self.DFS(i, adj_list, state):
                    return False
        return True
if __name__ == "__main__":
    s = Solution()
    print(s.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))