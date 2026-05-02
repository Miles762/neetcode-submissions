class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visit = set()



        res = 0
        
        def dfs(node):
            for nei in adjList[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)


        for i in range(n):
            if i not in visit:
                visit.add(i)
                dfs(i)
                res += 1

        return res

        

            

        