class Solution:
    def reverseWords(self, s: str) -> str:
        # idea: we start from the end of the string
        # make a left and right pointer at len(s) - 1, move left until you see a space
        # then make the substring from [left+1:right] and add to new string
        # edge cases:
        # multiple spaces between two words? -> reduce after creating substring, move left until not a space
        # leading spaces? -> we can use .strip() or simplify find when theres no longer a leading space and make new str

        s = s.strip() # O(n) time and space complexity
        
        n = len(s)
        left, right = n - 1, n
        res = []
        while left >= 0: # since we are going in reverse
            while left >= 0 and s[left] == " ":
                left -= 1

            right = left + 1 

            while left >= 0 and s[left] != " ":
                left -= 1

            res.append(s[left+1:right])
        
        return " ".join(res)
            
