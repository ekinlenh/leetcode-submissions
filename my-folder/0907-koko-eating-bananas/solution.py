class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # use binary search to determine a suitable speed below h hours
        # left = 1
        # right is determined by max in piles, which gives us the fastest time koko can eat all bananas

        min_speed = float('inf')

        left, right = 1, max(piles)
        while left <= right:
            speed = left + (right - left) // 2

            # check if this speed lets us eat all bananas under h hours
            hours = 0
            for num in piles:
                hours += (math.ceil(num / speed))
            
            print(hours)
            if hours <= h:
                right = speed - 1
                min_speed = min(min_speed, speed)         
            else:
                left = speed + 1
        
        return min_speed
