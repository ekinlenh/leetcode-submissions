class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute force:
        # for each bar, expand left and right to see what bars are >= current bar
        # this means that we can fill up those bars with the amoutn in current bar
        # then we can simply multiply current bar height * the expansion of right and left
        # Solution 1: O(n^2)
        # maxArea = 0
        # n = len(heights)
        # for i in range(n):
        #     # expand left
        #     left = i
        #     while left >= 0 and heights[left] >= heights[i]:
        #         left -= 1
        #     # expand right
        #     right = i
        #     while right <= n - 1 and heights[right] >= heights[i]:
        #         right += 1
        #     left += 1
        #     right -= 1
        #     maxArea = max(maxArea, heights[i] * (right - left + 1)
        # return maxArea
        # 
        # Solution 2:
        # use a monotonic stack, make it always be increasing because we want to see how far we can fill until we can't
        maxArea = 0
        stack = [] # store (height, index)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] >= h: # our current height is less than prev height, pop until not true
                height, index = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((h, start))
        
        # we still have items in our stack to compute area for
        for h, i in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
