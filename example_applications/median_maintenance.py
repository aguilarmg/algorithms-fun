from random import randint
from heapq import heappush, heappop
from math import fabs, inf
from statistics import median
from utils import *

N = 2**14

class medianMaintenance():

    def __init__(self):
        """
        Two invariants must be held:
            1. The size of the two heaps must be balanced (i.e., when 
               self.N % 2 == 0, then the two heaps must be of the same size, and
               when self.N % 2 == 1, then the two heaps' size must differ by
               only 1.
            2. The two heaps must be ordered. All elements of maxHeap must be
               < than all elements of minHeap.
        """
        self.minHeap = []
        self.maxHeap = []
        self.heapSizeDiff = 0

    def insertVal(self, val):
        """
        Insert val into the values seen so far, and return the new median of
        the values seen so far.
        """
        insert = heappush
        extractMin = heappop

        if len(self.maxHeap) == 0 and len(self.minHeap) == 0:
            # If both heaps empty, just add value to maxHeap
            maxHeapMax = -inf
            minHeapMin = inf
        elif len(self.minHeap) == 0:
            # self.maxHeap has value, but self.minHeap has no value
            maxHeapMax = -1*self.maxHeap[0]
            minHeapMin = inf
        elif len(self.maxHeap) == 0:
            # self.minHeap has a value, but self.maxHeap has no value
            minHeapMin = self.minHeap[0]
            maxHeapMax = -inf
        else:
            maxHeapMax = -1*self.maxHeap[0]
            minHeapMin = self.minHeap[0]

        if val <= maxHeapMax:
            insert(self.maxHeap, -1*val)
            self.heapSizeDiff -= 1
        else:
            insert(self.minHeap, val)
            self.heapSizeDiff += 1
        
        # Rebalance, if needed.
        if self.heapSizeDiff < -1:
            # maxHeap is larger than the minHeap.
            # Pop from maxHeap and insert into minHeap.
            tmp = -1*extractMin(self.maxHeap)
            insert(self.minHeap, tmp)
            self.heapSizeDiff += 2
        elif self.heapSizeDiff > 1:
            # minHeap is larger than the maxHeap.
            # Pop from minHeap and insert into maxHeap.
            tmp = extractMin(self.minHeap)
            insert(self.maxHeap, -1*tmp)
            self.heapSizeDiff -= 2

        return self.returnMedian()

    def returnMedian(self):
        """
        Return the median of the array
        """
        # Return the median value
        if self.heapSizeDiff == 0:
            minHeapMin = self.minHeap[0]
            maxHeapMax = -1*self.maxHeap[0]

            return ( minHeapMin + maxHeapMax ) / 2
        elif self.heapSizeDiff == -1:
            # maxHeap is 1 element larger than minHeap
            return -1*self.maxHeap[0]
        else:
            # minHeap is 1 element larger than maxHeap
            return self.minHeap[0]


def genRandomIntArray(n):
    return [randint(0, n) for _ in range(n)]

def main():
    all_vals = genRandomIntArray(N)
    medianTracker = medianMaintenance()

    stream = []
    for (i, val) in enumerate(all_vals):
        if i % 1000 == 0:
            print(f"Round {i}")
        stream.append(val)
        medianFound = medianTracker.insertVal(val)
        if foundIncorrectMedian(stream, medianFound):
            print(f"FAIL. Proper median was {median(stream)}. You found: {medianFound}")
            exit(1)

    print(f"PASS: Not a single median found was incorrect.")


if __name__=='__main__':
    main()
