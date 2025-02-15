'''
Convert a binary search tree to a sorted double-linked list. We can only change the target of pointers, but cannot create any new nodes.
For example, if we input a binary search tree as shown on the left side of the Figure 1, the output double-linked list is shown on the right side.
'''
'''

class Treenode:
    def __init__(self):
        left: TreeNode
        right: TreeNode
def solve(tree):soln

params:
    tree : Node - represeents a BST
preconditions:
    -tree may be null
return:
    soln : Node - return the head of the linked list
postcondition:
    - soln is the head correct sorted form of the tree
constraints:
    - tree is a BST node
    - guranteed 2 children 
    - left subtree <= root 
     -right subtree > root
'''
def solve(root):
    #base case
    if not root:
        return None
    else:
        #In order traversal to construct the LLISt
        left_node = solve(root.left)
        if left_node:
            root.left = left_node
            left_node.right = root
        #Process the right subtree
        right_node = solve(root.right)
        if right_node:
            right_node.left = root 
            root.right = right_node

        return  right_node if right_node else root
solve(3)
