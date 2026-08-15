class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # brute force: nested for-loop
        n = len(nums)

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        
        # return False

        window_set = set()

        for i in range(n):
            if i > k:
                window_set.remove(nums[i - k - 1])
            
            if nums[i] in window_set:
                return True
            
            window_set.add(nums[i])
        
        return False

