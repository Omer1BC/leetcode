class Solution:
    def minSwaps(self, data: List[int]) -> int:

        def f(element):
            return element
        def getK(data):
            return Counter(data)[1]
            
        soln = len(data)
        k = getK(data)
        curr = 0
        l = 0
        for r in range(len(data)):
            joined = data[r]
            curr += f(joined)
            if r >= k:
                left = data[l]
                curr -= f(left)
                l += 1
            soln=min(soln,k-curr)
        return soln



        