'''

'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next
'''
k > len - not possible 
len // k  - nodes per segment

[1,2,3,4,5,6]  21 / 6 = 3 node per segment  21%6 = 3 leftover   abs(21-6) = 1

1111 1111 1111 1111 1111  r< 5
len % k - remaining 

'''
def split_protein_chain(protein, k):

    pass