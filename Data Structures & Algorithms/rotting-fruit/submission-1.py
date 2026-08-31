class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = collections.deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0: return 0

        minutes = 0 
        while q:
            for i in range(len(q)):
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(rows) and 
                        nc in range(cols) and 
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            if q:
                minutes += 1      
        return minutes if fresh == 0 else -1
