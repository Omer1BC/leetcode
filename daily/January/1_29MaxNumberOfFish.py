class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        soln = 0
        visit = set()
        #Dimensions
        ROWS,COLS = len(grid),len(grid[0])

        def oob(u):
            i,j = u
            return not (0<=i<ROWS and 0<=j<COLS)
        def nbr(u):
            i,j = u
            return [(i,j) for i,j in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]]
        #Treat all the valid cells as components, and find the max path sum
        def dfs(i,j):
            if oob((i,j)) or (i,j) in visit or grid[i][j] == 0:
                return 0
            visit.add((i,j))
            res = 0
            for v in nbr((i,j)):
                r,c = v
                res += dfs(r,c)

            res += grid[i][j]
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] > 0:
                    soln = max(soln,dfs(i,j))
        return soln
        

                    


        