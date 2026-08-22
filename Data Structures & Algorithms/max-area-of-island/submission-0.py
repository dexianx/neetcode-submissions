class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 

        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxIsland = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r, c))
            area = 1

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr in range(rows) and 
                    nc in range(cols) and 
                    grid[nr][nc] == 1 and 
                    (nr,nc) not in visit):
                        area += 1
                        q.append((nr,nc))
                        visit.add((nr, nc))
            return area 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    maxIsland = max(maxIsland, bfs(r, c))

        return maxIsland

                    