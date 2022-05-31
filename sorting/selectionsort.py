import random
from utils import *

N_ELEMS_MIN = 1
N_ELEMS_MAX = 2**16

def indexOfSmallestElement(db, i):
    min_value = db[i]
    min_idx = i

    for j in range(i, len(db)):
        if db[j] < min_value:
            min_value = db[j]
            min_idx = j

    return min_idx

def swap(db, i, j):
    tmp = db[i]
    db[i] = db[j]
    db[j] = tmp

def selectionsort(db):
    """
    Input: an array of `n` numbers, in arbitrary order.
    Output: an array of the same numbers, sorted from smallest to largest
    ---
    Performs a linear scan through the input array to identify the minimum
    element, swaps it with the first element in the array, does a second scan
    over the remaining `n-1` elements to identify and swap into the 2nd position
    the second-smallest element, and so on.
    Each scan takes time proportional to the number of remaining elements, so
    the overall running time is O(n^2).
    """
    i = 0
    n = len(db)
    
    while i != n:
        # Find the smallest element in the array from [i:]
        idx_of_smallest_elem = indexOfSmallestElement(db, i)
        # Swap with the element in position i
        swap(db, i, idx_of_smallest_elem)
        # Increment i
        i += 1

    return db


def main():
    db = genRandomIntArray(N_ELEMS_MIN, N_ELEMS_MAX)
    print(f"array:\n{db}")
    sorted_db = selectionsort(db)
    print(f"proper sorted db:\n{sorted(db)}\n")
    print(f"selection sort of the arr:\n{sorted_db}")

    testForMismatches(sorted_db, sorted(db))

if __name__=='__main__':
    main()
