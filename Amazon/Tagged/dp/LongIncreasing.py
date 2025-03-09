'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

'''

'''
precond:
    -nums may not be none
constraints:
    - sub sequence is formed by deleting elements in the array
    - if no increasing subseq found, return 0
analysis:
    -time: O(n^2)
    - space: O(n)

'''
def solve(nums:List[int]) -> int:

    cache = [0]*len(nums)
    soln = 1
    for i in range(len(nums)-1,-1,0):
        n = nums[i] #Candidate number where extending the subsequence is possible
        longest = 0
        for j in range(i+1,len(nums)): #Can we extend the subsequence
            if nums[j] <= n: #Invalid candidate
                continue
            longest = max(longest,cache[j])
        cache[i] = longest + 1 #Extend the long subsequnece for this number
        soln = max(soln,cache[i])
    return soln

        


            
