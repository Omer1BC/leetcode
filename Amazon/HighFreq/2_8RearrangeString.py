class Solution:
    def reorganizeString(self, s: str) -> str:
        S = ""
        heap = [(-v,k) for k,v in Counter(s).items()]
        heapq.heapify(heap)
        while heap:

            count,c = heapq.heappop(heap)
            if count == 0:
                continue
            if c == S[-1] if S else "":
                if heap:
                    count_other,alt = heapq.heappop(heap)
                    S+= alt
                    heapq.heappush(heap,(count,c))
                    heapq.heappush(heap,(count_other+1,alt))
                else:
                    return ""
            else:
                S+= c
                heapq.heappush(heap,(count +1,c))
        return S