class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we need to determine which section to check:
        # either the nums[k] -> nums[n - 1] or the nums[0] -> nums[k - 1]
        # once we find this distinction we can use binary search to find the target
        # to do this, i think we need to find the dip (i.e. it goes from 7 to 0 in example 1)
        # actually, while doing binary search and the left pointer is greater than the target
        # then we can change the left to middle b/c we don't want to look at the section from 
        # left to middle

        left = 0
        right = len(nums) - 1

        while (left <= right):
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return middle

            if nums[left] <= nums[middle]: # this section is sorted
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1 # search left section
                else:
                    left = middle + 1 # search right section
            else: 
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1 # search right section
                else:
                    right = middle - 1 # search left section

        return -1
