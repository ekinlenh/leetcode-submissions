class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # we can use a max-heap, storing (val, index)

        res = []
        max_heap = []

        start = 0
        for end in range(len(nums)):
            heapq.heappush(max_heap, (-nums[end], end))

            if (end - start + 1) == k:
                while max_heap[0][1] < start:
                    heapq.heappop(max_heap)
                res.append(-max_heap[0][0])
                start += 1
        
        return res
