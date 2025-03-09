'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally 
or vertically neighboring. The same letter cell may not be used more than once in a word.
'''
'''
precond:
    -board is not none, neither is words
    -rows and cols are not none
    -no empty string words 
constraint:
    -baord mxn
    -not necessarily 
    -priortize time and space
'''
#Define the trie
class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
    #Add operation
    def add(self,word):
        root = self
        for c in word:
            #If we don't find a node to it, create it from root
            if c not in root.children:
                root.children[c] = Trie()
            root = self.children[c]
        root.end = True #Mark the node is found
    
    
            
def solve(board: List[List[str]],words: List[str]) -> List[str]:
    root = Trie()
    soln = []
    ROWS = len(board)
    COLS = len(board[0])
    moves = [(0,1),(0,-1),(1,0),(-1,0)]
    #Add all the words to a trie
    for word in words:
        root.add(word)

    def dfs(i,j,rt,local):
        #If found the end of the word
        if rt.end:
            soln.local(local[:])
        
        #Explore all the possible valid paths to words in the trie
        for char in rt.children:
            for dx,dy in moves:
                r = i + dy
                c = j + dx 
                if (0<=r<ROWS and 0<=c<COLS) and board[r][c] == char:
                    local.append(char)
                    dfs(r,c,rt.children[char],local)
                    local.pop()
    #Init the dfs search on valid cells
    for i in len(COLS):
        for j in len(ROWS):
            if board[i][j] in root.children:
                dfs(i,j,root,[])
    return soln

                     


    