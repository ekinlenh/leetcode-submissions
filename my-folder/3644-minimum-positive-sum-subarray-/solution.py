class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # brute force: 
        # nested for loop

        min_sum = float('inf')

        for start in range(len(nums)):
            curr_sum = 0
            for end in range(start, len(nums)):
                curr_sum += nums[end]
                length = end - start + 1
                if (l <= length <= r) and (curr_sum > 0):
                    min_sum = min(min_sum, curr_sum)
        
        return min_sum if min_sum != float('inf') else -1
