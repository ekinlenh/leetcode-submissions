class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}

        # make count map
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        max_length = 0
        for num in count:
            # add count[num] + count[num + 1]
            length = 0
            if num + 1 in count:
                length = max(length, count[num] + count[num + 1])

            max_length = max(max_length, length)
        
        return max_length
