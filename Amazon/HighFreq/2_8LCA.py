# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        vals = set([node.val for node in nodes])
        def h(root):
            if not root or root.val in vals:
                return root
            else:
                left = h(root.left)
                right = h(root.right)
                if not left:
                    return right
                if not right:
                    return left
                return root
        return h(root)
            


        
        