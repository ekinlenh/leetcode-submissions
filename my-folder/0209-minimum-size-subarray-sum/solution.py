class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # variable sliding window 
        # keep track of a window_sum
        # when window_sum < target, subtract left value and increment left until valid again
        # then check size of min window possible >= target

        window_sum = 0
        start = 0
        min_ = float('inf')

        for end in range(len(nums)):
            window_sum += nums[end]

            while window_sum >= target:
                min_ = min(min_, end - start + 1)
                window_sum -= nums[start]
                start += 1
        
        return 0 if min_ == float('inf') else min_

