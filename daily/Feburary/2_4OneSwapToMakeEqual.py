class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        '''
        def solve(str,str) -> bool
        
        params:
            s1 : one string
            s2 : another string 
        precondition:
            -s1, s2 not null
            - len(s1,s2) > 1
        return:
            soln : true/false whether s1 can be tranformed into s1 (or vice versa) by one swap
        postcondition:
            -soln is consistent with s1 and s2 being 1 swap apart
        constraints:
            -len of both s1,s2 > 1
            -size of s1 and s2
            -swap is 2 indicies that are swapped
                -indicies may be same  
        '''
        def swap(i,j):
            s1[i],s1[j] = s1[j],s1[i]
        
        #Check if strings are uneven lengths
        if (len(s1) != len(s2)):
            return False
        s1 = list(s1)
        s2 = list(s2)
        swaps = 0
        #Init the 2 pointers which will move inwards from the edges
        i,j = 0,len(s1)-1
        while i <= j:
            while  i <= j and s1[i] == s2[i]:
                i+=1
            while i <= j and s1[j] == s2[j]:
                j-=1
            #Swap is needed
            if i <= j:
                if swaps >= 1:
                    return False
                swap(i,j)
                if s1[i] == s2[i] and s1[j] == s2[j]: #Swap is successful
                    swaps+=1 
                else: #Swap was useless
                    return False     
        return swaps <= 1

                

        