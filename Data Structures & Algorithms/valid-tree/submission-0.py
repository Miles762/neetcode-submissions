class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n:
            return True
        visitSet = set()
        neighMap = {i:[] for i in range(n)}
        for n1, n2 in edges:
            neighMap[n1].append(n2)
            neighMap[n2].append(n1)

        def dfs(n,prev):
            if n in visitSet:
                return False
            visitSet.add(n)

            for i in neighMap[n]:
                if i == prev:
                    continue
                if not dfs(i , n):
                    return False
            return True

        return dfs(0, -1) and len(visitSet) == n
