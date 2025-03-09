'''
Given an array of integers nums and an integer k, return the number of contiguous subarrays 
where the product of all the elements in the subarray is strictly 
less than k.
'''

'''
precondition:
    -nums is not null
    -nums may not be empty
constraints:
    -return 0 for not solution
    -product < k 
analysis:
    -time: O(n)
    -space: O(1) 

'''
def solve(nums:List[int],k:int) -> int:

    #Init meta variables
    c = 0
    l = 0
    prod = 1
    #Loop through the nums array

    for r in range(len(nums)):
        joined = nums[r]
        prod *= joined 
        while l <= r and prod >= k: #Contract
            left = nums[l]
            prod = prod // left
            l += 1
        #Check if the window is valid
        c += r-l+1
    return c






