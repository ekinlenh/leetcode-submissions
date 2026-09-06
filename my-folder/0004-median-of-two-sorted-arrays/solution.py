class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        res = []
        first, second = 0, 0
        while first < len(nums1) and second < len(nums2):
            if nums1[first] < nums2[second]:
                res.append(nums1[first])
                first += 1
            else:
                res.append(nums2[second])
                second += 1

        if first < len(nums1):
            for i in range(first, len(nums1)):
                res.append(nums1[i])
        
        if second < len(nums2):
            for i in range(second, len(nums2)):
                res.append(nums2[i])

        # now we have a sorted res array
        # find median in this new array
        index = (len(res) - 1) // 2
        if len(res) % 2: # is odd
            return res[index]
        else:
            return (res[index] + res[index + 1]) / 2

