import random
from heapq import heappush, heappop, heapify
from utils import *

N_ELEMS_MIN = 1
N_ELEMS_MAX = 2**16

def heapSort(A):
    insert = heappush
    extractMin = heappop

    n = len(A)
    H = []
    # The insert(H, A[i]) requires O(logn) time, and it is performed n times,
    # so the following runs in time proportional to O(nlogn).
    for i in range(n):
        insert(H, A[i])
    
    B = []
    # The extractMin(H) requires O(logn) time, and it is performed n times,
    # so the following runs in time proportional to O(nlogn).
    for i in range(n):
        B.append(extractMin(H))

    # The first loop can be replaced by the following, which runs in
    # O(n) time.
    # heapify(A) # Transform A into a heap, in-place, in linear time. 
    # print(A)
    # B = []
    # # This loop would still run in O(nlogn) time, however.
    # for i in range(n):
    #     B.append(extractMin(A))
    
    return B

def main():
    db = genRandomIntArray(N_ELEMS_MIN, N_ELEMS_MAX)
    print(f"array:\n{db}")
    std_sorted_db = sorted(db)
    sorted_db = heapSort(db)
    print(f"proper sorted db:\n{std_sorted_db}")
    print(f"heap sort of db:\n{sorted_db}")

    testForMismatches(sorted_db, std_sorted_db)

if __name__=='__main__':
    main()
