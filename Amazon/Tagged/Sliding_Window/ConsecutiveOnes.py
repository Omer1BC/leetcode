'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array 
if you can flip at most k 0's.
'''

'''
precond:
    -nums can not be null
    -nums may be empty
        - return 0
constraints
    -nums is a binary array
'''

def solve(nums:List[int],k:int) -> int:
    
