'''
All nodes along children pointers from root to leaf nodes form a path in a binary tree. 
Given a binary tree and a number, please print out all of paths where the sum of all nodes value is same as the given number. 
The node of binary tree is defined as:
'''

'''
class Node:
    def __init__():
        left,right : Node

def solve(root,n): 
params:
    root: Node - represents the root of the tree
precond:
    -root may be null
return:
    -
postcond:
    -print out of all the nodes that form a path that add up to n
constraints:
    -values may be positive or negative
    -n may be any value 

'''

#Psuedo code
'''
soln = []
def solve(rt,n,local):
    if rt is none:
        if n is 0, append local to soln
        return 
    if n is negative
        return
    else:
        append rt to local
        call solve(rt.left,n-rt.data,local)
        call solve(rt.right,n-rt.data,local)
        pop rt       
'''
#Set of nodes that sum up to n
soln = []
def solve(root,n,local):
    #Found a set of nodes that form a valid path
    if not root:
        if n == 0:
            soln.append(local)
        return
    #Overshot the sum
    if n < 0:
        return
    else:
        #Potentially back track to find the solution
        local.append(root)
        solve(root.left, n-root.data,local)
        solve(root.right, n-root.data,local)
        local.pop()
for nodes in soln:
    for node in nodes:
        print(node.data)

solve(root,n,[])
        

