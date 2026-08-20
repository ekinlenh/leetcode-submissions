class Solution:
    def isValid(self, s: str) -> bool:
        # use a dict to store pairs
        brackets = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        # use a stack to ensure LIFO stands for valid parentheses
        # because the last used open bracket needs the first closed bracket
        stack = []
        for c in s:
            if c in brackets: # is an open bracket
                stack.append(brackets[c]) # add the closing bracket related to it
            else: # it's a closing bracket, check to see if it's the right one
                if len(stack) > 0 and c == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False

