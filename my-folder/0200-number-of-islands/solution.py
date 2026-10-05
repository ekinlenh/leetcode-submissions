class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # traverse through graph, 
        # run explore when you see a 1 that is not visited
        # and add to island count

        n = len(grid)
        m = len(grid[0])

        def dfs(seen, row, col):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            stack = [(row, col)]
            while stack:
                pair = stack.pop()
                seen.add((pair[0], pair[1]))

                for d in directions:
                    nr = pair[0] + d[0]
                    nc = pair[1] + d[1]

                    if nr >= 0 and nr < n and nc >= 0 and nc < m and (nr, nc) not in seen:
                        if grid[nr][nc] == '1':
                            stack.append((nr, nc))

        islands = 0
        seen = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i,j) not in seen:
                    islands += 1
                    dfs(seen, i, j)
                     
        return islands
