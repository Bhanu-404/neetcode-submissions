# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, maximum, minimum):
            if root is None:
                return True
            if not (minimum < root.val < maximum):
                return False
            
            return helper(root.left, root.val, minimum) and helper(root.right, maximum, root.val)
        return helper(root, float("infinity"), float("-infinity"))