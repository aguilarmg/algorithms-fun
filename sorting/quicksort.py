import random
from utils import *

"""
Quicksort:
    - Pick a pivot in the array
    - Create a subarray containing all of the elements < pivot, and create
      a subarray containing all of the elements > pivot [ this is O(N) ]
    - Call quicksort recursively on the two subarrays [ if subarrays are
      roughly half the length of the original array, then O(NlogN) ]
        - If pivot always leads to an array that is len(arr)-1 elems long, then
          runtime is O(N^2)
    
-- Base case:
    - If len(arr) == 0, return arr
    - If len(arr) == 1, return arr
    --- if len(arr) < 2, return arr

-- Recursive case:
    - Pick a pivot
    - Create subarrays around the pivot
    - Call quicksort recursively on the subarrays

"""

def quicksort(arr):
    n_elems = len(arr)

    if n_elems < 2:
        # Base case
        return arr
    else:
        # Recursive case
        # Pick a pivot randomly
        pivot_i = random.randint(0, n_elems-1)
        pivot_elem = arr[pivot_i]

        # Create subarrays around the pivot
        smaller_elems_subarr = []
        greater_elems_subarr = []
        for (j, elem) in enumerate(arr):
            if j == pivot_i:
                # Skip over pivot
                continue
            if elem <= pivot_elem:
                smaller_elems_subarr.append(elem)
            else:
                greater_elems_subarr.append(elem)

        # Call quicksort recursively on the subarrays
        left_sorted = quicksort(smaller_elems_subarr)
        right_sorted = quicksort(greater_elems_subarr)
        return [*left_sorted, pivot_elem, *right_sorted] 

def main():
    exp = random.randint(4, 8)
    n = random.randint(0, 2**exp)
    print(f"array will be {n} elements long.")
    db = [random.randint(0, 512) for _ in range(n)]
    print(f"array:\n{db}")
    sorted_db = quicksort(db)
    print(f"proper sorted db:\n{sorted(db)}\n")
    print(f"d&c max of the arr:\n{sorted_db}")

    testForMismatches(sorted_db, sorted(db))

if __name__=='__main__':
    main()
