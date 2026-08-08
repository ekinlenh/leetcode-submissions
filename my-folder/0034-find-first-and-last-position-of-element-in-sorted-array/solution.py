class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # The first task we need to do is find where exactly the target is located
        # We can use binary search, cutting the array in half first and seeing if 
        # the target lies in the left section or the right section.
        # We can continue this until we find the target value. 
        # Once we find it, we can expand left/right to see if it continues
        # Issue: this results in a O(n) solution to expand and find the range
        # How do we reduce this to O(log n)?
        # What if instead of exploring linearly left and right, we can do
        # binary search to the left/right of the middle target to find the 
        # starting point and ending point of the range

        res = []
        left = 0
        right = len(nums) - 1
        while left <= right: # Initalize binary search to find target
            middle = left + (right - left) // 2
            
            if nums[middle] < target: # We want to search the right section
                left = middle + 1
            elif nums[middle] > target: # We want to search the left section
                right = middle - 1
            else: # Perform the search range
                # O(n) approach not valid, but good for visualizing the process
                # res = [middle, middle]
                # search_left = middle - 1
                # search_right = middle + 1
                # while nums[search_left] == nums[middle]:
                #     res = [search_left, middle]
                #     search_left -= 1
                # while nums[search_right] == nums[middle]:
                #     res = [search_left, search_right]
                #     search_right += 1
                res = [middle, middle]
                if (middle - 1) >= 0: # We should explore left of middle
                    # Binary search from [left, middle]
                    search_left = left
                    search_right = middle
                    while search_left <= search_right:
                        new_middle = search_left + (search_right - search_left) // 2
                        if nums[new_middle] < target:
                            search_left = new_middle + 1
                        elif nums[new_middle] > target:
                            search_right = new_middle - 1
                        else:
                            res[0] = new_middle
                            search_right = new_middle - 1 # To see if there's another occurence to the left to find first
                if (middle + 1) < len(nums): # We should explore right of middle
                    # Binary search from [middle, right]
                    search_left = middle
                    search_right = right
                    while search_left <= search_right:
                        new_middle = search_left + (search_right - search_left) // 2
                        if nums[new_middle] < target:
                            search_left = new_middle + 1
                        elif nums[new_middle] > target:
                            search_right = new_middle - 1
                        else:
                            res[1] = new_middle
                            search_left = new_middle + 1 # To see if there's another occurence to the right to find last
                return res

        # No range found
        return [-1, -1]        
