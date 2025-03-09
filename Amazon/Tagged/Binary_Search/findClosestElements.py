'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
'''

'''
precondition:
    -arr can not be null
constraints:
    -arry can not be an empty array
    -return the result in ascending order
    -graded based on absolute value, if there's a tie, take the smaller element
    -array is sorted

'''
def solve(arr:List[int],k:int,x:int) -> List[int]:

