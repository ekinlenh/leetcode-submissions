class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # fixed-sliding window of size k
        n = len(nums)
        if k > n:
            return -1
        
        # make first section
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # loop through rest subarrays
        for i in range(k, n):
            window_sum += nums[i]
            window_sum -= nums[i - k]

            max_sum = max(max_sum, window_sum)

        return max_sum / k
        
