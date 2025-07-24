# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def BuildTrees(start, end):
            
            trees = []

            #Creating left and right subtrees
            if start>end:
                return [None]
            for i in range(start,end+1):
                left_subtrees = BuildTrees(start,i-1)
                right_subtrees = BuildTrees(i+1, end)

                for l in left_subtrees:
                    for r in right_subtrees:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r

                        trees.append(node)
            return trees
        return BuildTrees(1,n)