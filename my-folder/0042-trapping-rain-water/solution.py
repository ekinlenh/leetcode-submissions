class Solution:
    def trap(self, height: List[int]) -> int:
        # we need a way to find how much water accumulates at each section
        # at each bar, the amount of water that can be at that bar is dependent
        # on the max height to its left and max height to its right
        # so we can make two arrays leftHeights and rightHeights which each store
        # the max height at each bar and then we take the minimum of that to determine
        # the amount of water that can be stored at that specific bar
        # then we total up the amount of water that can be stored fro the whole map 

        n = len(height)
        leftHeights = [0] * n
        rightHeights = [0] * n

        for i in range(0, n):
            if i == 0:
                leftHeights[i] = height[0]
            else:
                leftHeights[i] = max(height[i], leftHeights[i - 1])
        
        for i in range(n - 1, -1, -1):
            if i == (n - 1):
                rightHeights[i] = height[i]
            else:
                rightHeights[i] = max(height[i], rightHeights[i + 1])
        
        print(leftHeights, rightHeights)
        totalWater = 0
        for i in range(n):
            min_height = min(leftHeights[i], rightHeights[i]) - height[i]
            totalWater += min_height
            print(totalWater)
        
        return totalWater
