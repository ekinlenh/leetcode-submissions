class TimeMap:
    # idea:
    # have a hashmap
    # key: string
    # value: tuples (value, timestamp)
    # values is always increasing because of time
    # set(): append new tuple to hashmap
    # get(): use binary search to find largest timestamp_prev

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        def condition(mid) -> bool:
            return self.map[key][mid][1] > timestamp

        left, right = 0, len(self.map[key])
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        if left == 0:
            return ""

        return self.map[key][left - 1][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
