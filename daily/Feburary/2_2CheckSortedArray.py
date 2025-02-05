class Solution:
    def check(self, nums: List[int]) -> bool:
        r = 0
        #Pop off the left sorted half elements
        while r < len(nums) and nums[r] >= (nums[r-1] if r > 0 else float('-inf')):
            r+= 1
        first = r
        #Pop off the right sorted half
        while r< len(nums) and nums[r] >= (nums[r-1] if r > first else float('-inf')) and nums[r] <= nums[0]:
            r+= 1
        #Array is empty
        if r == len(nums):
            return True
        else:
            #Remaining elements that are unordered
            return False
        
