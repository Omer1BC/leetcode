'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:
Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
'''

'''
precond:
    -nums is not none
    -leng of nums is postive
constraints:
    -solution is in O(logn)
    -nums is in sorted ascending order
    -values are unique
'''
def solve(nums:List[int]) -> int:
    