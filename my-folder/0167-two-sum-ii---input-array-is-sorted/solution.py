class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # idea: using two pointers
        # if the sum is greater than target, decrease right
        # if the sum is less than target, increase left

        left, right = 0, len(numbers) - 1
        while left < right:
            add = numbers[left] + numbers[right]
            if add > target:
                right -= 1
            elif add < target:
                left += 1
            else:
                return [left + 1, right + 1]
        
        return [-1, -1]
