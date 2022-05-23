class Solution:
      
    def numIslands(self, grid: List[List[str]]) -> int:
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        def find_land():
            for i in range(m):
                if "1" in grid[i]:
                    t = grid[i].index("1")
                    grid[i][t] = "0"
                    return i, t

        m = len(grid)
        n = len(grid[0])
        cnt = 0
        q = []
        while True:
            if not q:
                t = find_land()
                if not t:
                    break
                cnt += 1
                q.append(t)

            r, c = q.pop(0)
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < m and 0 <= nc < n) or grid[nr][nc] == '0':
                    continue
                q.append((nr, nc))
                grid[nr][nc] = "0"
        return cnt              
