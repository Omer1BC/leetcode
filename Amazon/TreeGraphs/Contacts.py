'''
We're going to make our own Contacts application! The application must perform two types of operations:

add name, where  is a string denoting a contact name. This must store  as a new contact in the application.
find partial, where  is a string denoting a partial name to search the application for. It must count the number of contacts starting with 
 and print the count on a new line.
Given  sequential add and find operations, perform each operation in order.
'''

'''
precond:
    -add and find operations are formatted properly
    -all lowercase
    -input may not be null
    -input <command> <name> 
postcond:
    -print the result of all counts 'The are _ for find of _'
constraints:
    -len(input) > 0
'''
#Define a trie 
class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
    #Adding a contact
    def add(self,contact):
        node = self
        for c in contact:
            if not c in node.children:
                node.children[c] = Trie()
            node = node.children[c] 
        node.end = True
    def find(self,prefix):
        res = [0]
        node = self
        for c in prefix:
            if c not in node.children:
                return res[0]
            node = node.children[c]
        self.search(node,res)
        return res[0]

    #Find all the words begin with prefix ending at node
    def search(self,node,local):
        #Found a valid word for the prefix
        if node.end == True:
            local[0] += 1
        for c in node.children.keys():
            self.search(node.children[c],local)
def solve(input:List[str]):
    #Parsing the input
    database = Trie()
    for word in input:
        tokens = word.split(" ")
        command,name = tokens[0],tokens[1]
        if command == "add":
            database.add(name)
        else:
            result = database.find(name)
            print(f'There are {result} for find of {name}')

        


        
