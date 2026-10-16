# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-infinity")
        def helper(root):
            if root is None:
                return 0
            
            left = max(0, helper(root.left))
            right = max(0, helper(root.right))
            self.max_sum = max(self.max_sum, root.val + left + right)
            return root.val + max(left, right)
        helper(root)
        return self.max_sum