'''
Given a binary search tree and a value k, please find a node in the binary search tree whose value is closest to k.
'''
'''
preconditions:
    - root may or may not be null
    - k may not be found
postcond:
    - returns the value closest to k in bst
constraints:
    - root is the root of bst 
    - left subtree  <=
    - right subtree >
'''
def solve(root:TreeNode,k:int) -> int:
    #Init a running list
    nums = []
    soln = k
    
    def inorder(rt):
        if not rt:
            return
        else:
            inorder(rt.left)
            nums.append(rt.val)
            if rt.val >= k:
                return
            inorder(rt.right)
    if len(nums) >= 2:
        diff1 = k - nums[-2]
        diff2 = k - nums[-1]
        #return the element with the smaller difference
        return nums[-2] if diff1 < diff2 else nums[-1]

    else:
        #Return the only element
        return nums[-1]


    
        

