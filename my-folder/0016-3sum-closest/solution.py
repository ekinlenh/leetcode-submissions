class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # like 3Sum, we want to sort the nums array
        # the difference now is that we want to check for a difference between 
        # three indices sum and the actual target and we want the lowest difference

        closest = nums[0] + nums[1] + nums[2] # will store the three integers that we can just sum at the end
        nums.sort() # to make it easier to traverse and find closest to target
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                ans = nums[i] + nums[left] + nums[right]
                
                diff = abs(target - ans)
                if diff < abs(target - closest):
                    closest = ans
                    
                if ans > target:
                    right -= 1
                else:
                    left += 1
                
        return closest
