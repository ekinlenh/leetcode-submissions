class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # idea: use a monotonic stack (increasing)
        # we are allowed to pop from the stack at most k times

        if k == len(num):
            return "0"

        stack = []
        for n in num:
            while stack and int(stack[-1]) > int(n) and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)        

        # edge case: stack already in increasing order and k is still > 0
        # then remove from the right b/c that's the greater values
        while k > 0:
            stack.pop()
            k -= 1

        res = ''.join(stack).lstrip('0') or '0'
        return res
