
''' 

Given a dictionary, a method to do lookup in dictionary and a M x N board where every cell has one character. 
Find all possible words that can be formed by a sequence of adjacent characters. Note that we can move to any of 8 
adjacent characters, 
but a word should not have multiple instances 
of same cell.

'''
'''
def solve(dictionary,matrix)
    params:
        dictionary:List[str] - it's a dicitonary of words 
        matrix: List[List[int]] - each cell has a character
    precondition:
        -m is not none and contains valid characters
        -matrix has only valid characters
    postconditions:
        -print all the found words
    constraints:
        -can only move vertically,horizontally,diagonally 
        -mxn may not be a square
        -characters are upper case lower case
        -all the words are unique in the matrix
'''

def solve(dictionary,matrix):
    #extracting the dimensions
    m = len(matrix)
    n = len(matrix[0])

    visit = set()

    def oob(i,j):
        return not (0<=i<m) or not (0<=j<n)
    def moves(i,j):
        return [(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i-1,j-1),(i+1,j+1),(i-1,j+1),(i+1,j-1)]
    def dfs(i,j,word):
        #Base cases, improper cells 
        if len(word) == 0:
            return True
        if oob(i,j) or (i,j) in visit or matrix[i][j] != word[0]:
            return False
        visit(i,j)
        for move in moves(i,j):
            x,y = move 
            #If dfs is successful, don't explore other branches
            if dfs(x,y,word[1:]):
                return True
            visit.remove(i,j)
        return False
    #finding the optimal starting point for each word 
    for word in dictionary:
        for i in range(len(m)):
            for j in range(len(n)):
                if (i,j) in visit:
                    continue
                if matrix[i][j] == word[0]:
                    if dfs(i,j,word):
                        print(word)
                
            

