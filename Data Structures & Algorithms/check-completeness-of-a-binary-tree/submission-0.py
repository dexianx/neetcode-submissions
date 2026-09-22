# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        seen_gap = False
        while q:
            node = q.popleft()
            if not node:
                seen_gap = True
                continue
            if seen_gap:
                return False
            q.append(node.left)
            q.append(node.right)
        return True
