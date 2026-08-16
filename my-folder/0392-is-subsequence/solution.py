class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # we are comparing s to t
        # we should find s[0] in t, then move onto s[1] on remaining chars in t, etc.
        # therefore set up a pointer for indicies in s that moves when we find the corresponding char in t
        # we loop through all elements in t and if the pointer indices is equal to len(s) then we return true, else false

        # edge cases
        if len(s) == 0: # "" is in every string
            return True

        if len(t) == 0:
            return False


        # idx = 0
        # for i in range(len(t)):
        #     if idx == len(s):
        #         return True

        #     if t[i] == s[idx]:
        #         idx += 1
        
        # return idx == len(s)

        # New approach: use a queue filled with chars from s, if queue is empty by end of traversal, we found result
        queue = deque(s)
        
        for char in t:
            if queue and char == queue[0]:
                queue.popleft()
        
        return not queue
        
