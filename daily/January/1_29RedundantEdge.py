class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #Number of nodes
        N = len(edges) + 1
        D = [1]*N
        P = [-1]*N
        def find(a):
            if P[a] == -1:
                return a
            else:
                P[a] = find(P[a])
                return P[a]
        #Join 2 nodes as a part of the same set
        def union(a,b):
            r1,r2 = find(a),find(b)
            #Found redundant connection
            if r1 == r2:
                return False
            else:
                #Merge the 2 sets based on roots 
                if D[r1] > D[r2]:
                    P[r2] = r1
                    D[r1] += D[r2]
                else:
                    P[r1] = r2
                    D[r2] += D[r1]
                return True
        
        for edge in edges:
            a,b = edge
            #Return the first failed occurence of a bad edge
            if not union(a,b):
                return edge
        return []