class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
                    visited.add((r,c))
        
        def explore(r,c):
            if (r<0 or r>= rows or c<0 or c>=cols or 
                grid[r][c]==-1 or (r,c) in visited):
                return
            visited.add((r,c))
            q.append((r,c))

        depth = 0
        while q:
            currInQueue = len(q)
            for i in range(currInQueue):
                r,c = q.popleft()
                grid[r][c] = depth
                explore(r+1,c)
                explore(r,c+1)
                explore(r-1,c)
                explore(r,c-1)
            depth+=1

