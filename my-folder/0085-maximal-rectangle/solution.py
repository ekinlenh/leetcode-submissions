class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # make a histogram for each row in the matrix
        # first row: [1, 0, 1, 0, 0], max area = 1
        # second row: [2, 0, 2, 1, 1], max area = 3
        # third row: [3, 1, 2, 2, 2], max area = 6
        # fourth row: [4, 0, 0, 1, 0], max area = 4
        
        maxArea = 0
        n = len(matrix[0])
        histogram = [0] * n
        for row in range(len(matrix)):
            stack = [] # still holds (height, index)
            for i, col in enumerate(matrix[row]):
                if col == '1':
                    histogram[i] += 1
                else: # i goes back to 0 if the new row has a 0 for that column
                    histogram[i] = 0
            
                # calculate max area of this histogram
                start = i
                while stack and stack[-1][0] >= histogram[i]:
                    height, index = stack.pop()
                    maxArea = max(maxArea, height * (i - index))
                    start = index
                stack.append((histogram[i], start))

            for h, i in stack:
                maxArea = max(maxArea, h * (n - i))

        return maxArea
