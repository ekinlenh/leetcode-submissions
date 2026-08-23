class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a deque (monotonic)
        # indices are sorted left -> right, while also carrying current val
        # until we get to size k, we want to append (val, index)
        # we keep the deque in decreasing order, pop all vals less than the val we add to the window
        # the max val will always be at deque[0][0] which we only pop when window size == k and we move it

        res = []
        dq = deque()

        start = 0
        for end in range(len(nums)):
            # maintain decreasing order
            while dq and dq[-1][0] <= nums[end]:
                dq.pop()

            # add element at end to window
            dq.append((nums[end], end))

            # check if window size == k
            if (end - start + 1) == k:
                if dq and dq[0][1] < start:
                    dq.popleft()
                res.append(dq[0][0])
                start += 1
        
        return res
