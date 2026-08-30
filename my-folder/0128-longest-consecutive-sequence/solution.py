class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()

        max_length = 0
        for num in nums:
            seen.add(num)
        
        for num in seen:
            length = 0
            # check if num is start of sequence
            if num - 1 not in seen:
                while (num + length) in seen:
                    length += 1
            
            max_length = max(max_length, length)

        return max_length
