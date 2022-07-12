import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)
        

    def addNum(self, num: int) -> None:

        if not self.min_heap:
            heapq.heappush(self.min_heap, num)
            return 

        min_heap_top = self.min_heap[0]
        if num >= min_heap_top: 
            heapq.heappush(self.min_heap, num)
        else: 
            heapq.heappush(self.max_heap, -num)

        if len(self.min_heap) - len(self.max_heap) > 1: 
            item = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -item)
        elif len(self.max_heap) - len(self.min_heap) > 1: 
            item = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -item)

    def findMedian(self) -> float:
        
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]

        elif len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]

        median = self.min_heap[0] - self.max_heap[0]
        median = median / 2
        
        return median
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()