class Solution:
  def islandsAndTreasure(self, grid: List[List[int]]) -> None: 
    # store the treasures in a queue and do bfs in reverse. 
    ROWS, COLS = len(grid), len(grid[0])
    q = collections.deque()
    visited = set()

    def addCell(r, c):
      if (r not in range(ROWS) or 
        c not in range(COLS) or 
        (r, c) in visited or 
        grid[r][c] == -1
      ):
        return 
      else:
        visited.add((r, c))
        q.append((r, c))
      

    for r in range(ROWS):
      for c in range(COLS):
        if grid[r][c] == 0:
          q.append((r,c))
          visited.add((r, c))

    division = 0
    while q:
      for i in range(len(q)):
        r, c = q.popleft()
        grid[r][c] = division 
        addCell(r-1, c)
        addCell(r + 1, c)
        addCell(r, c - 1)
        addCell(r, c + 1)
      division += 1


      
      