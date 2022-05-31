# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root, 1)])
        while q:
            cur, d = q.popleft()
            if not cur.left and not cur.right:
                return d
            if cur.left:
                q.append((cur.left, d+1))
            if cur.right:
                q.append((cur.right, d+1))
                
            
        