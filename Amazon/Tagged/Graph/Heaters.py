'''
Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range. 

Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

Notice that all the heaters follow your radius standard, and the warm radius will the same
'''

'''
preconditions:
    -houses may be empty but not null
constraints
    -return -1 for no solution
    -houses[i] > 0
    -not sorted
analysis:
    time: O(nlogn)
    space: O(1)

'''
def solve(houses:List[int]) -> int:
        #Init meta information 
        c = 0
        dist = 0
        #Create a priority queue the distances left to right
        
        heapq.heapify(houses)
        while houses:
            dist = houses[0] + 2
            c += 1
            #Popping invalid houses
            while houses and houses[0] <= dist:
                heapq.heappop(houses)
        return c