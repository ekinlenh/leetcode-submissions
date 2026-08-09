class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Three Parts of the Problem:
        # 1. Get a substring
        # 2. Check if said substring is a palindrome
        # 3. Keep count of the longest substring we see
        # Parts 2 and 3 are easy to do
        # Part 1 -> How should we tackle this?
        # One way is to start with a left and right pointer at the start of the string
        # If that is currently a palindrome, move the right pointer and check if that's a palindrome
        # Continue this process until it no longer becomes a palindrome
        # Once this happens, increment the left pointer and start again 
        # Repeat this process until we are done with the string
        # First Solution:
        # left = 0
        # right = left + 1
        # while (right < len(s)):
        #     substring = s[left:right]
        #     if isPalindrome(substring):
        #         right += 1
        #         if len(substring) > len(longestPalindrome):
        #             longestPalindrome = substring
        #     else:
        #         left += 1
        #         right += 1
        #
        # Test Cases:
        # 1. "a" -> substring = s[0:1] = "a", this is a palindrome, right += 1 & longestPalindrome = "a", and we stop
        # 2. "bab" -> "b" is a palindrome, but "ba" is not so we stop and move left to "a" -> but "bab" is a palindrome
        # 3. "abcd" -> we return ""
        # Current issue: We need to solve "bab", "baab", "baccab": the letters between
        # This is because we start at the front of the string
        # What if we start in the middle? And expand outward left and right?
        # This allows us to check if the left and right of an index is equal, therefore is a palindrome
        # New solution test cases:
        # "bab" -> i in range(1,2) -> i = 1
        # left = 0, right = 2, currentPalindrome = "a"
        # s[left] == s[right] -> currentPalindrome = s[0:3] = "bab" -> longestPalindrome = "bab"
        # New issue: "cbbd" -> How do we deal with even length strings?
        # There are two different cases: Even and Odd Length Strings
        # We should make two separate cases for them

        longestPalindrome = s[0] # A character is a palindrome in itself (s.length is guaranteed to be >= 1)

        for i in range(0, len(s)): # We iterate through all in-between characters
            left = i
            right = i
            currentPalindrome = s[i]
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currentPalindrome = s[left:right+1]
                left -= 1
                right += 1
                
                if len(currentPalindrome) > len(longestPalindrome):
                    longestPalindrome = currentPalindrome

            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currentPalindrome = s[left:right+1]
                left -= 1
                right += 1
                
                if len(currentPalindrome) > len(longestPalindrome):
                    longestPalindrome = currentPalindrome   


        return longestPalindrome
