class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # 'a' is always the smallest lexicographical character
        # so we can traverse the string until we don't see an 'a'
        # and change it to an 'a' and the palindrome should break

        res = list(palindrome)
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                res[i] = 'a'
                return ''.join(res)
        
        res[-1] = 'b'
        if len(palindrome) > 1:
             return ''.join(res)
        else:
            return ""
