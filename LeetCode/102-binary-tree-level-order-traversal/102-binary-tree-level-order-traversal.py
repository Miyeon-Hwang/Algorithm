# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        cur_level = [root]
        while cur_level:
            next_level = []
            cur_vals = []
            for n in cur_level:
                cur_vals.append(n.val)
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            res.append(cur_vals)
            cur_level = next_level
        return res
        