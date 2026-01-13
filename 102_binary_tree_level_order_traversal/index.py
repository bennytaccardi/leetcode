# Definition for a binary tree node.
from collections import deque
from http.cookiejar import cut_port_re
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        visited = set([])
        queue = deque()
        queue.append((root,0))
        solution = []
        if root:
            solution.append([root.val])
        while len(queue) > 0:
            current, distance = queue.popleft()
            if current and current not in visited:
                visited.add(current)
                print(f"Current: {current.val}")
                print(f"Distance: {distance}")
                queue.append((current.left, distance+1))
                queue.append((current.right, distance+1))
                if distance > 0:
                    if len(solution) > distance:
                        if solution[distance] is None:
                            solution.insert(distance, [current.val])
                        else:
                            solution[distance].append(current.val)
                    else:
                        solution.insert(distance,[current.val])
        return solution
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1

    while i < len(nodes):
        current = queue.pop(0)

        if i < len(nodes) and nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1

    return root

if __name__ == "__main__":
    root = build_tree([3,9,20,1,1,15,7])

    s = Solution()
    sol = s.levelOrder(root)
    print(sol)
