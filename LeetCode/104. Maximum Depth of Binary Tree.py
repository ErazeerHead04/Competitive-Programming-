# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
#another approach:
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node, depth):
            nonlocal result
            if node is None:
                result =  max(result,depth)
            else:
                dfs(node.left, depth+1) 
                dfs(node.right, depth+1)
        dfs(root,0)
        return result 

        