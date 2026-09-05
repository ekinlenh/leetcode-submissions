class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def condition(mid, right) -> bool:
            if nums[mid] <= nums[right]:
                return True

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if condition(mid, right):
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return left if nums[left] == target else -1
