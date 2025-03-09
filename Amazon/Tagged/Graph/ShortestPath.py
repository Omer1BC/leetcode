
'''
preconditions:
    -grid can not be null
    -grid is a sqaure matrix
    -1,0 for the values
constraints:
    -return shortest path length, else -1
    -8 directions
        -horizontally,vertically,diagonally
analysis:
    -time: O(n^2)
    -space: O(n)
'''
def solve(grid:List[List[int]]) -> int:
        #Init the variables for bfs
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        moves = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]

        src = (0,0)
        if grid[0][0] == 0:
            q.append((src,1))
        #Start the bfs, account for each type of cell
        while q:
            curr,d = q.popleft()
            i,j = curr
            if not(0<=i<ROWS and 0<=j<COLS)  or grid[i][j] == 1:
                    continue
            #Found the src
            if i == ROWS -1 and j == COLS -1:
                    return d
            grid[i][j] = 1
            for dx, dy in moves:
                r,c  = i+dx,j+dy
                q.append(((r,c),d+1))
        return -1