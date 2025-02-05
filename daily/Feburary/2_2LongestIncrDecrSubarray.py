class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        '''
        def solve(List[int]) -> int
        params:
            nums: list of numbers
        preconditions:
            - nums is non-null
            - size of nums is > 1
        return:
            soln: the longest subarray of either striclty increasing or decreasing numbers
        postcondition:
            soln is consistent with the true longest subarray

        constraints:
            - len(nums) >= 1
            - nums[i] can be negative
            - strictly increasing or decerasing meaning duplicates "stop" the subarray from expanding
            - soln >= 1
        '''
        #Initializing the running lengths for the subarrays for increasing and decreasing
        l_incr = m_incr = l_decr = m_decr = 1
        #Traverse nums checking for strictly increasing and decreasing
        for i in range(1,len(nums)):
            #Compare the running subarray that's increasing
            if nums[i] > nums[i-1]: #Improve increasing subarray size by one
                l_incr += 1
            else: #Not possible 
                l_incr = 1
            if nums[i] < nums[i-1]: #Improve the decreasing subarray size by one if possible
                l_decr += 1
            else:
                l_decr = 1
            m_incr = max(m_incr,l_incr)
            m_decr = max(m_decr,l_decr)

        return max(m_incr,m_decr)


        