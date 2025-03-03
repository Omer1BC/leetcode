'''
Given the root of a binary tree, the value of a target node target, and an integer k, 
return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
'''

'''
class TreeNode:
    -left,right: TreeNodes
    -val:int
precond:
    -root may be null
    -target will be found in the true
    -k may not have a solution
constraints:
    -root is a binary tree node
    -target is VALUE
    -empty list 
analysis:
    - Time: O(n)
    - Time O(n)
'''
def solve(root:TreeNode,target: int,k:int) -> List[int]:
    #Create an adj list
    adj = defaultdict(list)

    
    #recursively fill the list
    def create_list(parent,root):
        nbrs = adj[root.val]
        if parent != -1:
            nbrs.append(parent)

        #Pass the calls to valid children
        if root.left:
            nbrs.append(root.left.val)
            create_list(root.val,root.left)
        if root.right:
            nbrs.append(root.right.val)
            create_list(root.val,root.right)
        
    #Init bfs variables
    q = deque()
    visit = set()
    depth = 0
    if root:
        q.append(target)
        visit.add(target)
        create_list(-1,root)
    #Iterate layer by layer on queue until desired depth is met
    while q and depth < k:
        #process the current layer
        for _ in range(len(q)):
            curr = q.popleft()
            for nbr in adj[curr]:
                if nbr not in visit:
                    q.append(nbr)
                    visit.add(nbr)
        depth += 1
    #K may be too large, so no solution
    return list(q)

    

    



    