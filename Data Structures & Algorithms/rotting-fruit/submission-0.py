class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        steps = 0
        q = deque()
        
        def explore(r,c):
            if(r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!=1):
                return
            
            grid[r][c]=2
            q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
        
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                explore(r,c+1)
                explore(r+1,c)
                explore(r-1,c)
                explore(r,c-1)
            if q:
                steps+=1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return -1
        
        return steps