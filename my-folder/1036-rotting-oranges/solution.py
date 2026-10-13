class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # idea:
        # run BFS until all oranges are explored from rotten ones
        # keep count of minutes (breadth level)
        # then afterward check the grid again to see if any fresh ones exist
        # if not, return minutes, else -1

        rows = len(grid)
        cols = len(grid[0])

        def bfs(queue):
            directions = [
                [1,0],
                [-1,0],
                [0,1],
                [0,-1]
            ]

            minutes = 0
            while queue:
                size = len(queue)
                for _ in range(size):
                    r, c, distance = queue.popleft()

                    for d in directions:
                        nr, nc = r + d[0], c + d[1]

                        if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                            if grid[nr][nc] == 1: # is fresh orange
                                grid[nr][nc] = 2 # make it rotten
                                queue.append([nr, nc, distance + 1])
                                minutes = distance + 1
                
            return minutes + 1
        
        # use multi-source BFS approach, add all sources
        # then we will automatically get the best minute for each orange
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append([row, col, 0])
        
        minutes = bfs(queue)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1

        return minutes - 1
