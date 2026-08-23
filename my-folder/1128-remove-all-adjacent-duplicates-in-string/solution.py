class Solution:
    def removeDuplicates(self, s: str) -> str:
        # use a stack to store the most recent letter
        # if the letter we append is equal to the top letter in the stack
        # we should pop from the stack and not add that new letter
        # at the end of the traversal, we should be left with non-adjacent duplicates in the string

        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if stack[-1] == c:
                    stack.pop()
                else:
                    stack.append(c)
            
        return ''.join(stack)
