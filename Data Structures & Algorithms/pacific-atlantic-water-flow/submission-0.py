class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        rows,cols = len(grid), len(grid[0])
        pac = [[False] * cols for _ in range(rows)]
        atl = [[False] * cols for _ in range(rows)]
        pacific = []
        atlantic = []
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        for r in range(rows):
            pacific.append((r,0))
            atlantic.append((r,cols-1))
        for c in range(cols):
            pacific.append((0,c))
            atlantic.append((rows-1,c))

        def bfs(src, dest):
            q = deque(src)
            while q:
                r,c = q.popleft()
                dest[r][c] = True
                for xR,xC in directions:
                    dR,dC = r+xR,c+xC
                    if(0<=dR<rows and 0<=dC<cols and 
                        not dest[dR][dC] and grid[dR][dC]>=grid[r][c]):
                        q.append((dR,dC))

        bfs(pacific,pac)
        bfs(atlantic,atl)
        res = []
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])
        return res