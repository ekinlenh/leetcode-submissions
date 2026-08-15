class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        count = {}

        for num in nums1:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        for num in nums2:
            if num in count and count[num] != 0:
                res.append(num)
                count[num] -= 1
        
        return res
