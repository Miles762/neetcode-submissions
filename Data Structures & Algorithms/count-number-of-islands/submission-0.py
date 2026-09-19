class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                row,col = q.popleft()
                Directions = [[-1,0],[0,1],[1,0],[0,-1]]
                for dr,dc in Directions:
                    r = row + dr 
                    c = col + dc
                    if (r in range(rows) and c in range(cols)) and ((r,c)) not in visit and grid[r][c] == "1":
                        q.append((r,c))
                        visit.add((r,c))


        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == "1":
                    bfs(r,c)
                    islands+=1
        return islands

        
        