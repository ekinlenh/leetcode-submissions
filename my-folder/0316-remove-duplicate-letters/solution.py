class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # idea: 
        # we only want to start appending once we find the smallest lexicographical char
        # maybe we can first find the index of this and traverse through the rest of the string
        # if we want the smallest in lexicographical order, we could use an increasing stack
        # and pop from the stack when the new char we add is less than the top of the stack
        # i.e. stack = ["a", "c"], if we want to append "b", we pop "c" so stack = ["a", "b"]
        # but for example 2, the expected output is "acdb" so how do we get this from our stack?

        # stores the last occurrence index of each char in s
        last_occur = {}
        for i, c in enumerate(s):
            last_occur[c] = i     

        seen = set()
        stack = []
        for i, c in enumerate(s):
            if c not in seen:
                seen.add(c)
                while stack and stack[-1] > c and last_occur[stack[-1]] > i:
                    seen.remove(stack.pop())
                stack.append(c)
        
        return ''.join(stack)
