'''
The median of a set of integers is the midpoint value of the data set for which an equal number of integers are less than and greater than the value. 
To find the median, you must first sort your set of integers in non-decreasing order, then:

If your set contains an odd number of elements, the median is the middle element of the sorted sample. In the sorted set ,  is the median.
If your set contains an even number of elements, the median is the average of the two middle elements of the sorted sample. In the sorted set ,  is the median.
Given an input stream of  integers, perform the following task for each  integer:

Add the  integer to a running list of integers.
Find the median of the updated list (i.e., for the first element through the  element).
Print the updated median on a new line. The printed value must be a double-precision number scaled to  decimal place (i.e.,  format).
'''

'''
precond:
    - nums is not none
postcond:
    - Print the successive medians of each updated list after adding an element from nums
constraints:
    - length of nums > 0 
'''
import heapq
def solve(nums:List[int]) -> float:

    #init the heaps
    lh = []
    rh = []

    #helper methods
    def insert(n):  
        heapq.heappush(lh,-n)
        #Satisfy the elments in lh <= rh
        if rh and rh[0] <= -lh[0]:
            heapq.heappush(rh,-heapq.heappop(lh))
        #Uneven heaps 
        if len(lh) > len(rh)+1:
            heapq.heappush(rh,-heapq.heappop(lh))
        if len(rh) > len(lh)+1:
            heapq.heappush(lh,-heapq.heappop(rh))
    #Calculate the median given the size of the heaps
    def getMedian():
        if len(lh) == len(rh):
            return (-lh[0] + rh[0])/2
        else:
            return -lh[0]

    for n in nums:
        insert(n)
        median = getMedian()
        print(median)
    
        


