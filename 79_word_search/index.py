from collections import deque
from typing import List, Tuple

Node = Tuple[int, int]
class Solution:
    def find_node(self, board: List[List[str]], element: str) -> List[Tuple[int, int]]:
        sol: List[Tuple[int, int]] = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == element:
                    sol.append((i,j))
        return sol

    def find_all_neighbors(self, board, node: Tuple[int, int]) -> List[Tuple[int, int]]:
        neighbors = [(node[0]-1, node[1]), (node[0], node[1]-1), (node[0], node[1]+1), (node[0]+1, node[1])]
        for n in neighbors.copy():
            if n[0] < 0 or n[0] > len(board) -1 or n[1] < 0 or n[1] > len(board[0])-1:
                neighbors.remove(n)
        return neighbors

    def DFS (self, board: List[List[str]], node: Node, visited: List[Node], word: str, current_word: str):
        visited.append(node)
        current_word += board[node[0]][node[1]]
        if current_word not in word:
            visited.remove(node)
            return False
        if current_word == word:
            return True
        neighbors = self.find_all_neighbors(board, node)
        for n in neighbors:
            if n not in visited:
                if self.DFS(board, n, visited, word, current_word):
                    return True
        visited.remove(node)
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        unique_chars = set(word)
        for u_c in unique_chars:
            if len(self.find_node(board, u_c)) == 0:
                return False
        root_nodes = self.find_node(board, word[0])
        if len(root_nodes) == 0:
            return False
        for r_n in root_nodes:
            res = self.DFS(board, r_n, [], word, "")
            if res:
                return True
        return False
if __name__ == "__main__":
    sol = Solution()
    res = sol.exist(board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], word = "AAAAAAAAAAAAAAa")
    print(res)