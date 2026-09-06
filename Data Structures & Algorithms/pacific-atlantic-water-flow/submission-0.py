class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # main idea do dfs from each of the oceans and mark them. 
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()


        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or 
            r not in range(rows) or 
            c not in range(cols) or
            heights[r][c] < prevHeight ):
                return 

            visit.add((r,c))
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                dfs(nr, nc, visit, heights[r][c])


        # go to each row in the pacific and atlantic
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r,c])

        return res