'''
precond:
    -colors.len > 1
    -always 1 or 0 colors[i]
    -k > 3
constraints:
    -colors is circular
    -window of k must alternate
        -by this, except the edges, colors[i] alternates with its right and left neighbor
    -return the number of such windows
'''
def solve(colors:List[int],k:int) -> int: 
    soln = 0
    n = len(colors)
    size = 1
    for r in range(1,n+k-1):
        size = size + 1 if not colors[r%n] == colors[(r-1)%n] else 1
        soln += 1 if size >= k else 0
    return soln 