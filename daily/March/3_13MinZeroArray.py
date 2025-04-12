
'''
precond:
    -nums.len > 1
    -val_i in query > 1
    -query.len > 1
    -nums[i] >= 0
constraints:
    -decrement each value by at most val_i if it falls within range
    -vali can be chosen independently
    -return the smallest k after which nums becomes 0 array
    --1 if no solution NOT 0
    -range ins inclusive if idx is at li, query applies
def solve(nums:List[int],queries: List[List[int]]) -> int:
'''
def minZeroArray(nums:List[int],queries:List[List[int]]) -> int:
    Q = len(queries)
    N = len(nums)

    def valid(k):
        diff = [0] * N
        for i in range(k):
            l,r,v = queries[i]
            diff[l] += v
            if r < N-1: diff[r+1] -=v
        s = 0
        for i in range(N):
            s += diff[i]
            if s < nums[i]:
                return False
        return True
    l,r = Q,0
    while l >= r:
        k = l - (l-r)//2
        print(k,l,r)
        if valid(k):
            l = k - 1
        else:
            r = k + 1
    return r if r <= Q else -1