class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        #Total pairs 
        n = len(nums)
        total = n*(n-1)//2
        m = defaultdict(int)
        good = 0
        for i,v in enumerate(nums):
            #Precomputed i-nums[i] for previous elements determines the good pairs
            diff = i -v
            good += m[diff]
            m[diff] += 1
        return total - good


