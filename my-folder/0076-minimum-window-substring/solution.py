class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # variable sliding window
        # once we the count of chars of t == count of chars in s, we decrease window size
        # updating min window while possible
        
        s_map = {}
        t_map = {}
        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)
            s_map[c] = 0
        
        res = [-1, -1] # stores start and end index

        matches = 0
        start = 0
        for end in range(len(s)):
            if s[end] in s_map:
                s_map[s[end]] += 1
                # if we have enough of that letter
                if s_map[s[end]] == t_map[s[end]]:
                    matches += 1

            # once the substring contains t
            while matches == len(t_map):
                # update substring indices if possible
                length = end - start + 1
                if res[0] == -1:
                    res[0], res[1] = start, end
                else:
                    if length < (res[1] - res[0] + 1):
                        res[0], res[1] = start, end
                # update our window map
                if s[start] in s_map:
                    s_map[s[start]] -= 1
                    if s_map[s[start]] < t_map[s[start]]:
                        matches -= 1

                start += 1
        
        return s[res[0]:res[1] + 1]
                
