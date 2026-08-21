class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # division truncates -> //
        # no division by zero check needed
        # idea:
        # we can use a stack that we store elements in until we reach an operator
        # i.e. in example 1, stack = [2, 1] "+" -> 2 + 1 = 3 -> append this back onto the stack
        # we always pop the first two elements from our stack when we encounter an operator
        # and we append that result back into the stack to ensure it's used for the next operator
        # this takes care of situations like "4, 13, 5, /" where 13 / 5 is done first before 4 + (13 / 5)

        stack = []
        for token in tokens:
            if token in "+-*/":
                if len(stack) < 2:
                    return 0
                second_num = stack.pop()
                first_num = stack.pop()

                if token == "+":
                    stack.append(first_num + second_num)
                elif token == "-":
                    stack.append(first_num - second_num)
                elif token == "*":
                    stack.append(first_num * second_num)
                elif token == "/":
                    stack.append(int(first_num / second_num))
            else: # append integer to our stack for future operations
                stack.append(int(token))
        
        return stack[-1]
