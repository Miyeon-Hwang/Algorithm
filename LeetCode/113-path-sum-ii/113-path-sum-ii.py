# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        def dfs(cur, path):
            path.append(cur.val)
            
            if not cur.left and not cur.right and sum(path) == targetSum:
                answer.append(path)
                return
            
            if cur.left:
                dfs(cur.left, path[:])
            if cur.right:
                dfs(cur.right, path[:])
        
        answer = []
        dfs(root, [])
        return answer
        