class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # for each window, we want to keep track of the max value
        # we can do this using a max-heap
        # to make sure the max always stays in bounds in the window range
        # we track the index of each max_value
        # when window_size == k, we pop from heap until a valid max
        # then we can move the window to the right one posiiton

        max_heap = []
        heapq.heapify(max_heap)

        res = []
        start = 0
        for end in range(len(nums)):
            heapq.heappush(max_heap, (-nums[end], end))
            if (end - start + 1) == k:
                # go until valid max value in window
                while max_heap[0][1] < start or max_heap[0][1] > end:
                    heapq.heappop(max_heap)
                # valid max_value
                res.append(-max_heap[0][0])
                start += 1
        
        return res
