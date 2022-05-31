# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, cur_n):
            cur_n = cur_n * 10 + node.val
            if not node.left and not node.right:
                nums.append(cur_n)
                return
            if node.left:
                dfs(node.left, cur_n)
            if node.right:
                dfs(node.right, cur_n)
        
        nums = []
        dfs(root, 0)
        return sum(nums)