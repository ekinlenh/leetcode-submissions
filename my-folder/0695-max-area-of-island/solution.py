class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        def dfs(row, col):

            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

            stack = [[row, col]]

            area = 0
            while stack:
                cell = stack.pop()

                r, c = cell[0], cell[1]

                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]

                    if nr >= 0 and nr < n and nc >= 0 and nc < m:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 0 # change to 0 so we don't explore in future
                            stack.append([nr, nc])

                area += 1

            return area

        max_area = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    max_area = max(max_area, dfs(row, col))

        return max_area               
