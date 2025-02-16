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
class Treenode:
    def __init__(self,data=0,left=None,right=None):
        self.left  = left
        self.right = right
def solve(root):
    #base case
        stack = []
        curr = root
        prev = None
        first = None
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if not prev:
                    first = curr
                else:
                    prev.right = curr
                    curr.left = prev
                    curr = prev
                curr = curr.right

        return  right_node if right_node else root
solve(3)
