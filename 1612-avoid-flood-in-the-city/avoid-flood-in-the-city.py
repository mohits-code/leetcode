class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dry_days = []
        floods = {}
        res = [-1] * len(rains)

        for i in range(len(rains)):
            curr = rains[i]

            if curr > 0:
                if curr in floods:
                    if not dry_days:
                        return []
                    
                    found = False
                    temp = []

                    while dry_days:
                        day = heapq.heappop(dry_days)
                        if day > floods[curr]:
                            res[day] = curr
                            found = True
                            break
                        else:
                            temp.append(day)

                    for d in temp:
                        heapq.heappush(dry_days, d)

                    if not found:
                        return []
                floods[curr] = i

            else:
                heapq.heappush(dry_days, i)

        while dry_days:
            res[heapq.heappop(dry_days)] = 1

        return res
