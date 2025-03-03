'''
Given a tree and an integer, k, in one operation, we need to swap the subtrees of all the nodes at each depth h, where h ∈ [k, 2k, 3k,...].
In other words, if h is a multiple of k, swap the left and right subtrees of that level.

You are given a tree of n nodes where nodes are indexed from [1..n] and it is rooted at 1. 
You have to perform t swap operations on it, and after each swap operation print the in-order 
traversal of the current state of the tree.
'''
'''
class TreeNode:
    -left,right: TreeNode
precond:
    -root may be null
    -k > 0
postcond:
    -print the result of the swapped trees at each level
constraints:
    -if depth of root < k we don't swap
'''
def solve(root:TreeNode,k:int):

    def helper(root,d):
        nonlocal k
        # base case
        if not root:
            return
        else:
            #Either invert the calls to 'swap' subtrees, or proceed in regular inorder
            if d + 1 % k == 0: #If the next depth is a multiple, swap calls
                helper(root.right,d+1)
                print(root.val)
                helper(root.left,d+1)
            else:
                #Regular inorder
                helper(root.left,d+1)
                print(root.val)
                helper(root.right,d+1)

    helper(root,1)
    return 
