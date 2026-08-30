class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # idea:
        # use a hashmap to keep count of each integer
        # track a most_frequent
        # traverse through hashmap with frequency as the key to a list
        # populate a res list with hashmap 

        freq = {}
        count = {}
        most_freq = 0
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            most_freq = max(most_freq, count[num])
        
        for key in count:
            if count[key] not in freq:
                freq[count[key]] = []
            freq[count[key]].append(key)

        res = []
        while k > 0:
            if most_freq in freq:
                n = freq[most_freq]
                if len(n) > 0:
                    res.append(n.pop())
                    k -= 1
                else:
                    most_freq -= 1
            else:
                most_freq -= 1

        return res

