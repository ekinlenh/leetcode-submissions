class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1, 2, 3] -> [1, 3, 2]
        # We need to find the next lexicographically greater permutation
        # Why is [1, 3, 2] the next one? -> Because after [1, 2, 3], we want to keep the 1 but swap 3 and 2
        # Because they are the only options available. What is the trick behind this?
        # We are grabbing the smallest greater number of the index we want to change (i.e. nums[1] = 2)
        # We look to the right of this index and see if there is a value and in this case there is (nums[2] = 3)
        # Because of that, we swap it with the 2 to get [1, 3, 2]
        # What about a bigger array?
        # [1, 4, 2, 3] -> [1, 4, 3, 2]
        # First we looked at the last index (nums[3] = 3) but there's nothing to its right
        # Therefore we go back to index 2 (nums[2] = 2) and notice 3 > 2 so we swap them 
        # Therefore we get [1, 4, 3, 2] after [1, 4, 2, 3]
        # So the way we get the next permutation is to first start at the end of the array
        # And at each index, look to its right to see if there's a larger value (if so, we can swap)
        # The swap should only happen at the very end though once we're sure

        # The thinking above doesn't work, let's fix it
        # [1, 4, 7, 6, 5, 2] -> [1, 5, 2, 4, 6, 7]
        # In this example, we can see multiple swaps being made
        # But notice how we are swapping at index 1 (nums[1] = 4) and after that we have [7, 6, 5, 2]
        # This is in decreasing order so once we swap 4 and 5, we'll have [7, 6, 4, 2] which is NOT
        # the next permutation. The next permutation should have [2, 4, 6, 7].
        # Notice how it swaps from decreasing to increasing order. 
        # For us to have swapped at index 1, it meant that everything to its right was already the largest rearrangement.
        # So we just need to find this index i that is swapped and also reverse the order of the numbers to its right.
        # To do this, we can check if nums[i] < nums[i + 1], avoiding repeated comparisons as we know there's a larger
        # arrangement at this index.

        for i in range(len(nums) - 2, -1, -1): # Reverse order traversal
            # Find the smallest increase
            if nums[i] < nums[i + 1]:
                j = len(nums) - 1
                while nums[j] <= nums[i]: # Get swap element
                    j -= 1
                
                nums[i], nums[j] = nums[j], nums[i]
                nums[i+1:] = nums[i+1:][::-1] # Reverse everything to the right of the swap value
                return
        
        # If we exit the for loop without finding the pivot it means the array is currently the largest rearrangement
        # And we need to reverse the whole array
        nums.reverse()


