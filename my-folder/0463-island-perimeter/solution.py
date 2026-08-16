class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # brute force: nested for loop
        # if grid[i][j] == 1 (is land)
        # check surrounding cells -> if there's water, perimeter += 1

        max_row = len(grid)
        max_col = len(grid[0])

        perimeter = 0

        for i in range(max_row):
            for j in range(max_col):
                if grid[i][j] != 1:
                    continue
                
                # check up
                if i - 1 < 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                
                # check left
                if j - 1 < 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                
                # check right
                if j + 1 >= max_col or grid[i][j + 1] == 0:
                    perimeter += 1
                
                # check down
                if i + 1 >= max_row or grid[i + 1][j] == 0:
                    perimeter += 1
        
        return perimeter

