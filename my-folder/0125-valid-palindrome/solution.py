class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        def checkAlphanumeric(s: str, index: int) -> bool:
            if ord('a') <= ord(s[index]) <= ord('z') or ord('0') <= ord(s[index]) <= ord('9'):
                return True
            
            return False

        s = s.lower()
        while left <= right:
            while left < right and not checkAlphanumeric(s, left):
                left += 1
            while left < right and not checkAlphanumeric(s, right):
                right -= 1

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        
        return True
