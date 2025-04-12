'''
preconditions:
    -blocks.len > 1
    -k > blocks.len
    -B,W for blocks[i]

constraints:
    -minimum number of operations
        -operation switchs w->b
def solve(blocks:str,k:int) -> int:

'''

def minimumRecolors(self, blocks: str, k: int) -> int:
    count = 0
    res = 0
    l = -k
    for i in range(len(blocks)):
        count += 1 if blocks[i] == "B" else 0
        #blocks start to leave
        if i >=k -1:
            res = max(res,count)
            count -= 1 if blocks[i+1-k] == "B" else 0
    return k - res

        