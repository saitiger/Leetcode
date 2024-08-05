import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.currSmallest = 1
        self.st = set()
        self.pq = []

    def popSmallest(self):
        if self.pq:
            result = heapq.heappop(self.pq)
            self.st.remove(result)
        else:
            result = self.currSmallest
            self.currSmallest += 1
        return result

    def addBack(self, num):
        if num >= self.currSmallest or num in self.st:
            return
        self.st.add(num)
        heapq.heappush(self.pq, num)
