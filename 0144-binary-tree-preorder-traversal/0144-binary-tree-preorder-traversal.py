# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        
        def traversal(node):
            ans.append(node.val)
            if node.left:
                traversal(node.left)
            if node.right:
                traversal(node.right)

        traversal(root)
        return ans