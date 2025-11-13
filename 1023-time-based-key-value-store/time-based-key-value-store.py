class TimeMap:

    def __init__(self):
        self.kvs=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kvs[key].append((timestamp,value))


    def get(self, key: str, timestamp: int) -> str:
        prev=-1
        l=0
        r=len(self.kvs[key])-1
        while l<=r:
            mid=(l+r)//2
            if self.kvs[key][mid][0]<=timestamp:
                prev=mid
                l=mid+1
            else:
                r=mid-1

        if prev==-1:
            return ""
        return self.kvs[key][prev][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)