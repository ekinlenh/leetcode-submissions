class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # idea:
        # the number of substrings formed consecutively by 1s and 0s
        # and have the same number of 0's and 1's
        # is the minimum between the # of 1s and 0s 
        # ex: 00100 [2, 1, 2]
        # min(2,1) = 1 + min(1,2) = 1 + 1 = 2 (01, 10)
        
        prev, curr, res = 0, 1,0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]: curr += 1
            else:
                res += min(prev, curr)
                prev = curr
                curr = 1
        
        return res + min(prev, curr)

