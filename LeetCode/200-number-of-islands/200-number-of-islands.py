class Solution:
      
    def numIslands(self, grid: List[List[str]]) -> int:
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        
        def bfs(r, c):
            if grid[r][c] == "0":
                return 0
            q = [(r,c)]
            while q:
                r, c = q.pop(0)
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if not (0 <= nr < m and 0 <= nc < n) or grid[nr][nc] == '0':
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"
            return 1

        m = len(grid)
        n = len(grid[0])
        cnt = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and bfs(r, c):
                    cnt += 1
        return cnt              
