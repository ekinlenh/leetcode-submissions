class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # brute force is O(n^3)
        # we can optimize to O(n^2) by using two pointers
        # first sort the array (to make it easier to find sums)
        # then, we can fix an index (using for loop)
        # and traverse to its right using left/right pointers
        # since we have a sorted array, we can simply find two integers
        # that when added to current index results in 0, else continue

        res = []

        seen = set()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                target = nums[i] + nums[left] + nums[right]
                if target < 0:
                    left += 1
                elif target > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while (left < right and nums[left] == nums[left - 1]):
                        left += 1
        
        return res
