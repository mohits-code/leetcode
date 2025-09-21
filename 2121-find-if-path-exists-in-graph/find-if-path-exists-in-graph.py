class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        parent=[i for i in range(n)]
        rank=[1] *n

        def find(i):
            res = i
            while res!=parent[res]:
                parent[res]=parent[parent[res]]
                res=parent[res]
            return res

        def union(i,j):
            rootI=find(i)
            rootJ=find(j)

            if rootI!=rootJ:
                if rank[rootI]>rank[rootJ]:
                    parent[rootJ]=rootI
                elif rank[rootI]<rank[rootJ]:
                    parent[rootI]=rootJ
                else:
                    parent[rootJ]=rootI
                    rank[rootI]+=1
                return True
            return False
        
        for u, v in edges:
            union(u, v)
        
        return find(source)==find(destination)


        