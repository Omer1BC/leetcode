'''
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

'''

'''
class TreeNode:
    -left,right: TreeNode
    -val : int
    -parent: TreeNode
precond:
    -root,p,q are non null
    -p,q must be found
constraints:
    -Tree is binary
analysis:
    -O(n) = time
    -O(h) = space 
'''
def solve(root:TreeNode,p:TreeNode,q:TreeNode) -> TreeNode:
    #Base cases
    if root == p or root == q:
        return root
    #Root is neither p or q, but is a leaf
    if not root or (not root.left and not root.right):
        return None
    #Bottom up recursion to find p,q 
    left = solve(root.left,p,q)
    right = solve(root.right,p,q)
    if not left:
        return right
    if not right:
        return left
    #This is the LCA
    return root
