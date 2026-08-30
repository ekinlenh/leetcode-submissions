class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_map = {}
        for c in s1:
            s1_map[c] = 1 + s1_map.get(c, 0)

        start = 0
        s2_map = {}
        for end in range(len(s2)):
            s2_map[s2[end]] = 1 + s2_map.get(s2[end], 0)

            # window condition
            while (end - start + 1) > len(s1):
                s2_map[s2[start]] -= 1
                if s2_map[s2[start]] == 0:
                    s2_map.pop(s2[start])
                start += 1
                
            if s1_map == s2_map:
                return True
            
        return False
