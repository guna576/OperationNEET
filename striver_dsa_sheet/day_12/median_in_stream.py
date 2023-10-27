class MedianFinder:
    def __init__(self):
        self.maxHeap=[]
        self.minHeap=[]

    def addNum(self, num: int) -> None:
        n1=len(self.maxHeap)
        n2=len(self.minHeap)
        if n1==n2:
            if num>self.findMedian():
                heappush(self.minHeap,num)
            else:
                heappush(self.maxHeap,-num)
        elif n1==n2-1:
            if num>self.findMedian():
                val=heappop(self.minHeap)
                heappush(self.maxHeap,-val)
                heappush(self.minHeap,num)
            else:
                heappush(self.maxHeap,-num)
        else:
            if num>self.findMedian():
                heappush(self.minHeap,num)
            else:
                val=-heappop(self.maxHeap)
                heappush(self.minHeap,val)
                heappush(self.maxHeap,-num)

    def findMedian(self) -> float:
        n1=len(self.maxHeap)
        n2=len(self.minHeap)
        if n1==n2-1:
            return self.minHeap[0]
        elif n2==n1-1:
            return -self.maxHeap[0]
        else:
            if n1==0 and n2==0:
                return 0
            return (-self.maxHeap[0]+self.minHeap[0])/2


# O(nlogn) and O(n)

# left side maxheap and rightside minheap