class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        '''
        def solve(List[int],List[int])->List[int]

        params:
            A: One permuation array
            B: Second permuation
        precondition
            no pre conditions 
            A,B are nonnull
        return:
            C: S.T. C[i] represents common elements between A,B up to index i
        postconditions:
            C would be the appropriate common prefix array returned
            C is always found
        constraints:
            length of A,B > 1, same size

            optimize both space and time complexity 

            0,1,2..i inclusive for C[i]

        '''
        N = len(A)
        C = [0]*N
        # Init a context window for all the numbers C has seen so far
        seen = set()
        count = 0
        # Loop through A,B in parallel
        for i in range(N):
            # A,B's current contriubtion 
            a = A[i]
            b = B[i]
            # We could have 'seen' either both elements, 1 element, or none

            if a in seen: #If we have seen a number before, another shared number
                count += 1 
            else:
                seen.add(a) # Else mark it as seen
            if b in seen: 
                count += 1
            else:
                seen.add(b)
            C[i] = count
        return C