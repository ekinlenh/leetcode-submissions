class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # idea:
        # use binary search to find which row the target number belongs to 
        # this is found out by if target is in range of first and last element in that row
        # then, once that row is found: use binary search on that row to find target
        # this runs in O(log n + log m) = O(log(n * m))
        # where n = number of rows and m = number of columns

        n = len(matrix) # rows
        m = len(matrix[0]) # cols

        r_left, r_right = 0, n - 1
        while r_left <= r_right:
            r_middle = r_left + (r_right - r_left) // 2

            if target < matrix[r_middle][0]: # search before this row
                r_right = r_middle - 1
            elif target > matrix[r_middle][m - 1]: # search after this row
                r_left = r_middle + 1
            else: # we found the row to search through
                c_left, c_right = 0, m - 1

                while c_left <= c_right:
                    c_middle = c_left + (c_right - c_left) // 2
                    if matrix[r_middle][c_middle] < target:
                        c_left = c_middle + 1
                    elif matrix[r_middle][c_middle] > target:
                        c_right = c_middle - 1
                    else:
                        return True

                return False

        return False
