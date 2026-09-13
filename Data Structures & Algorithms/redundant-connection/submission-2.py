class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        # for edge in edges:
        #     uf.unite(edge[0], edge[1])
        # print(uf)
        criminal = None
        for idx, edge in enumerate(edges):
            if not uf.unite(edge[0], edge[1]):
                return edge
        return -1
        # return edges[criminal] if criminal else -1

        
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size+1))

    def __str__(self):
        return str(self.parent)
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi == pj:
            return False
        self.parent[pi] = pj
        # return pi != 
        return True
