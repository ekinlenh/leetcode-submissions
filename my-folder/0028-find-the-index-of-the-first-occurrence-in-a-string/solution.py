class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # we can check each substring of len(needle) in haystack
        # this will give us O(n*m) time complexity where
        # n = len(needle) and m = len(haystack) and we create a 
        # substring during the while loop
        # edge case: will len(needle) always be less than len(haystack)?

        if len(needle) > len(haystack):
            return -1

        left_ptr = 0
        right_ptr = len(needle)

        while right_ptr <= len(haystack):
            s = haystack[left_ptr:right_ptr]
            if s == needle:
                return left_ptr
            
            left_ptr += 1
            right_ptr += 1
        
        return -1
