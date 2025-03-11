

'''
A queue of C/D where each can vote out the other. Return the winning side
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

'''
Print n+1 string so that I means that the next number is greater, D means next number is less

Options: 1-9
Restriciton: Lexographically smallest 
'''
def arrange_guest_arrival_order(arrival_pattern):
  count = 1
  order = []
  stack = []
  n = len(arrival_pattern)
  for i in range(1,n+2):
    print(arrival_pattern,i,n)
    stack.append(i)
    if  i== n+1 or arrival_pattern[i-1] == "I" :
      while stack:
        order.append(stack.pop())
  return order
print(arrange_guest_arrival_order("IIIDIDDD"))

