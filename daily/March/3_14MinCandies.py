'''
precond:
    -candies.len > 1
    -candies[i] > 1
    -k > 1
constraints:
    -no pile merging
    -each child gets n candies
    
'''
def maximumCandies(self, candies: List[int], k: int) -> int:
    total = max(candies)
    l,r = 1,total
    def valid(x):
        piles = 0
        for c in candies:
            piles += c // x if x > 0 else 0
        return piles >= k
    while l <=r:
        m = (l + r)//2
        if valid(m):
            l = m + 1
        else:
            r = m -1
    return r
        