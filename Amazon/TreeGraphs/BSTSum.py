'''
Given the root of a binary search tree and an integer k, return true if there exist two elements 
in the BST such that their sum is equal to k, or false otherwise.
'''

'''
precond:
    -root is the root of a bast
    -root may or may not be null
postcond:
    -return whether 2 such nodes have been found
constraints:
    -k is positive
'''
class Stack:
    def __init__(self,rt,order):
        self.inorder = order
        self.stack = []
        self.add(rt)

    def add(self,rt):
        while rt:
            self.stack.append(rt)
            rt = rt.left if self.inorder else rt.right
    #Must be non empty stack
    def pop(self):
        res = self.stack.pop()
        self.add(res.right if self.inorder else res.left)
        return res
    def hasNext(self):
        return self.stack
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        #Init the least and greatest in BST
        L,R = Stack(root,True),Stack(root,False)
        l,r = L.pop(),R.pop()

        #Decrement l,r according to the sum
        while L.hasNext() and R.hasNext() and l != r:
            sum = l.val + r.val
            if sum > k:
                r = R.pop()
            elif (sum < k):
                l = L.pop()
            else:
                return True
        return False
    

