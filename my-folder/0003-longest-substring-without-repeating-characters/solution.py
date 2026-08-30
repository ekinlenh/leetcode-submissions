class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # start from first index
        # add this char to a set (ensure no dupes)
        # if there is a dupe, expand from the left until there's no dupe
        # otherwise, add to set and continue expanding window right

        seen = set()
        max_length = 0

        start = 0
        for end in range(len(s)):
            # expand left to remove dupes in our window before adding
            while s[end] in seen:
                seen.remove(s[start])
                start += 1

            max_length = max(max_length, end - start + 1)
            seen.add(s[end])

        return max_length
