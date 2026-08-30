class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_prod = [1] * len(nums)
        for i in range(1, len(nums)):
            left_prod[i] = left_prod[i - 1] * nums[i - 1]
        
        right_prod = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            right_prod[i] = right_prod[i + 1] * nums[i + 1]
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = left_prod[i] * right_prod[i]
        
        return res
