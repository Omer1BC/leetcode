'''
Problem: Determine whether an input array is a post-order traversal sequence of a binary tree or not. If it is, return true; 
otherwise return false. Assume all numbers in an input array are unique.

For example, if the input array is {5, 7, 6, 9, 11, 10, 8}, true should be returned, since it is a post-order traversal
sequence of the binary search tree in Figure 1. If the input array is {7, 4, 6, 5}, false should be returned since there are no binary search trees whose post-order traversal sequence is such an array.
'''

'''
class TreeNode:
    - left, right: TreeNode
    - data : int
precond:
    - root may be none
    - nums may be empty
postcond:
    - return true or false whether nums is valid post order
constraints:
    -  may be incompatible sizes 
    -  may or may not be positive
'''
def solve(root: TreeNode,nums: List[int]) -> bool:
    i = 0
    soln = True
    # define the recursive function
    def h(rt):
        nonlocal i
        if not rt:
            return 
        #post order calls
        h(rt.left)
        h(rt.right)
        # If the solution is invalid
        if i >= len(nums) or rt.data != nums[i]:
            soln= False
        i = i +1
    h(root)
    return soln 
        


