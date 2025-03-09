'''
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
'''

'''
class TreeNode:
    left,right : TreeNode
    val: int
precond:
    -root can not be null
constraints:
    -top to bottom
analysis:
    -time: O(n)
    -space: O(n)

'''
def solve(root:Optional[TreeNode]) -> List[Optional[TreeNode]]:
