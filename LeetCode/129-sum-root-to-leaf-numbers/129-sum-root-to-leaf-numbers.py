# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, path):
            path.append(node.val)
            if not node.left and not node.right:
                nums.append(int("".join(map(str,path))))
                return
            if node.left:
                dfs(node.left, path[:])
            if node.right:
                dfs(node.right, path[:])
        
        nums = []
        dfs(root, [])
        return sum(nums)