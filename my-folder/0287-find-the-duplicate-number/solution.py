class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # we can use fast and slow pointers
        # we cycle through the nums list
        # eventually, the slow and fast pointer will equal each other 
        # but this means they could have came here from different indices
        # this will cause a constant cycle and output error
        # we can find the start of this cycle, which indicates what the dupe number is

        slow, fast = 0, 0
        # we know there is a duplicate so loop until we break
        while True:    
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break    
        
        # we found a cycle, now let's find the start of the cycle
        start = 0
        while start != slow:
            start = nums[start]
            slow = nums[slow]
        return start    
