

'''
precondition:
    -votes is never an empty string
    -only valid characters: C,D
constraints:
    -return "Dog Lovers" or "Cat Lovers"
analysis:
    -time: O(n)
    -space: O(n)
    -
'''
from collections import deque
def predictAdoption_victory(votes: str) -> str:
  
    #init the q
    c_q,d_q = deque(),deque()
    #add the voters to each q
    for c in votes:
        if c == "C":
            c_q.append(c)
        else:
            d_q.append(c)
    #proceed while neither q is empty
    first = votes[0]
    while c_q and d_q:
    #take turns popping
        if first == "C":
            c_q.popleft()
            d_q.popleft()
            first = "D"
        else:
            c_q.popleft()
            d_q.popleft()
            first = "C"
    return "Dog Lovers" if d_q else "Cat Lovers"
print(predictAdoption_victory("CD")) 
print(predictAdoption_victory("CDD")) 

