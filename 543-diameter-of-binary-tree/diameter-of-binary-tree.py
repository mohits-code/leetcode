# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max=0
        self.dfs(root)
        return self.max

    def dfs(self, node):
        if node is None:
            return 0
        l=self.dfs(node.left)
        r=self.dfs(node.right)

        self.max=max(self.max, l+r)

        return 1+max(l,r)

        


        