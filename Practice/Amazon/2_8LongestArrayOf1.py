class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        L = [0]*n
        R = [0]*n
        l,r = 1,n-2
        L[l-1] = nums[l-1]
        R[r+1] = nums[r+1]

        while l < n:
            r = n -1 - l
            if nums[l] == 0:
                L[l] = 0
            else:
                L[l] = L[l-1] + 1
            if nums[r] == 0:
                R[r] = 0
            else:
                R[r] = R[r+1] + 1
            l += 1
        soln = -1
        print(L)
        print(R)
        for i in range(len(nums)):
            left = L[i-1] if i > 0 else 0
            right = R[i+1] if i < n-1 else 0
            local = left + right if nums[i] == 1 else left + right + 1
            soln = max(soln,left+right)
        return soln


        

        