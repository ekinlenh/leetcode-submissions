class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def condition(mid, right) -> bool:
            # find where the lower section is 
            if nums[mid] < nums[right]:
                return True

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid, right):
                right = mid
            else:
                left = mid + 1
        
        return nums[left]
