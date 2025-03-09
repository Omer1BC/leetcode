'''
You are given the root of a binary tree with unique values, 
and an integer start. At minute 0, an infection starts from the node 
with value start.
Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.
'''
'''
class TreeNode:
    -left,right : TreeNode
preconditions:
    -root may not be null
    -root is also a root of binary tree
constraints:
    -adjacent meaning it is the child of a root node
    -infection starts from the node with value start
    -child can infect its parent
    -start will be in the tree

'''
def solve(root: TreeNode, start: int) -> int: 

    #Define bfs
    def bfs(rt,start):
        q = deque([(rt,0)])
        depth = 0
        start_depth = 0

        while q:
            #Process the current layer
            for _ in range(len(q)):
                temp,d = q.popleft()
                if temp.val == start:
                    start_depth = d
                depth = d
                if temp.left:
                    q.append((temp.left,d+1))
                if temp.right:
                    q.append((temp.right,d+1))
        return (start_depth,depth)
    depth1,depth2 = bfs(root,start)
    return depth1 + depth2
        




