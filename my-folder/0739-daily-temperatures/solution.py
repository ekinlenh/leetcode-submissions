class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # idea:
        # use a stack to store the previous temperatures (grab the indices)
        # while the current temperature is warmer, pop from stack 

        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            # current temperature is warmer than previous temperature
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                res[index] = i - index
            
            stack.append(i)
        
        return res
