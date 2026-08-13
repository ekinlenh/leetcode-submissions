class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute force method is O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] < nums[i]:
        #             temp = nums[i]
        #             nums[i] = nums[j]
        #             nums[j] = temp
        # how to improve this solution?
        # count number of 0s, 1s, and 2s in the array using a dict
        # then we can modify nums to represent this count of nums in order
        # count = {
        #     0: 0,
        #     1: 0,
        #     2: 0
        # }

        # for num in nums:
        #     count[num] = count.get(num) + 1
        
        # key = 0
        # for i in range(len(nums)):
        #     while count[key] == 0:
        #         key += 1
            
        #     nums[i] = key
        #     count[key] -= 1
        # how can we make a one-pass algorithm?
        # idea: bring zeros to the left, bring 2s to the right, this leaves 1s in the middle (sorted)
        left = 0
        right = len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0: 
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1
            


