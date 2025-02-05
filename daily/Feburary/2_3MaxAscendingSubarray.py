class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        """
        def solve(List[int]) -> int
        params:
            nums : an array of numbers
        precondition:
            -nums may not be null
            -nums is not empty
        return:
            soln: maximum sum of the longest increasing subarray
        postcondition:
            -soln is consistent with the true maximum subarray sum
        constraints:
            -len(nums) > 1
            -nums[i] may be negative
            -minimum size of a subarray is 1
            -increasing means strictly increasing (duplicates don't count)
        """
        # Initilize the variables, consider the first element as the tentative max

        curr = soln = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += nums[i]  # Expand the subarray to include this element
            else:
                curr = nums[i]  # Reset the subarray to be the current element

            soln = max(
                soln, curr
            )  # In case the max subarray has already been encoutered
        return soln
