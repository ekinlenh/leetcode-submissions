class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # fixed window of size = 10
        # in this window, we want to see if the substring occurs more than once in a DNA molecule
        # i have two ways of thinking how to acknowledge this if condition
        # 1. make a freq map each substring, can't store in sets but can store in lists to check with, O(n) time
        # 2. sort the string, use that as a key in the map, then check for new substrings if already in dict, O(nlogn)
        # let's do first way first because of better complexity
        # misread problem, it has to be the specific sequence, not just same substring
        # therefore we can store the substring in a set rather than use a map
        # then make seen = set() and res = set() to avoid dupes

        n = len(s)

        if 10 >= n:
            return []

        seen = set()
        res = set()

        # make first window of size 10
        seen.add(s[:10])

        # make rest windows
        start = 1
        for end in range(10, n):
            sequence = s[start:end+1]

            if sequence in seen:
                res.add(sequence)
            else:
                seen.add(sequence)
                        
            start += 1
            
        return list(res)
