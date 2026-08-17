class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # idea:
        # in the window, keep count of most frequent letter
        # window_size - most_frequent > k: means we have too many replacements needed
        # this means that we should move our left pointer rather than right pointer to increase length
        # if we can continue, then update max_length and continue moving right pointer

        n = len(s)
        count = {} # keep track of count of elements in window
        max_f = 0 # most frequent letter in our window
        max_length = 0 # max length found in string

        left = 0 # window starts here
        for right in range(n): # until right pointer reaches end of string, we check substrings
            count[s[right]] = 1 + count.get(s[right], 0) # update count for new letter
            max_f = max(max_f, count[s[right]])

            # check if our window has too many replacements needed
            if (right - left + 1) - max_f > k:
                count[s[left]] -= 1 # decrease the count before moving
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length

