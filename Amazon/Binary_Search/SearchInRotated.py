'''
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] 
(0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is 
not in nums.

You must decrease the overall operation steps as much as possible.
'''

'''
Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

preconditions:
    -nums is not none
    -len of nums >= 0
constraints:
    -nums is sorted
    -nums is rotated at a particular pivot
    -return whether a target is found
'''

def solve(nums:List[int],target:int) -> bool:
    #Init the variables
    n = len(nums)
    l,r = 0,n-1

    while l<= r:
        #compute the pivot
        m = (l+r)//2
        if nums[m] == target:
            return True
        if nums[l] <= nums[m]: #Middle falls in the left sorted portion
            #The serach space is determined based on the target relative to nums[l]
            if target < nums[l]:
                l = m+1
            else:
                r = m-1
        else:
            #Middle is in the right sorted portion
            if target > nums[r]:
                #Chceck the right portion
                r = m -1
            else:
                #Check the left portion
                l = m -1
    return False
        

            

    


