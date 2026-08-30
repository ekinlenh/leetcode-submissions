class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # very similar to 3 sum
        # except we want to keep track of the closest target (i.e. abs difference from target to sum)
        
        res = -1
        lowest_diff = float('inf')

        nums.sort() # sort nums again to make it easier to traverse
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                added = nums[i] + nums[left] + nums[right]
                diff = abs(target - added) # we want the closest diff as possible

                if diff < lowest_diff:
                    lowest_diff = diff
                    res = added
                
                # to traverse, i want to consider how i can make diff the lowest it can be
                if added < target:
                    left += 1
                elif added > target:
                    right -= 1
                else:
                    return added
                
        return res

