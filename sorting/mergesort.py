import random
from utils import *

N_ELEMS_MIN = 1
N_ELEMS_MAX = 2**16

def merge(left, right):
    i = 0
    j = 0
    res = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i != len(left):
        # Append any remaining items from the left array
        res.append(left[i])
        i += 1
    while j != len(right):
        # Append any remaining items from the right array
        res.append(right[j])
        j += 1
    return res


def mergesort(arr):
    n_elems = len(arr)
    mid_point = n_elems // 2

    if n_elems < 2:
        # Base case
        return arr
    else:
        # Recursive
        left = arr[0:mid_point]
        right = arr[mid_point:]
        merge_left = mergesort(left)
        merge_right = mergesort(right)
        merged = merge(merge_left, merge_right)
        return merged

# def foundMismatches(x, y):
#     if len(x) != len(y):
#         return True
#     else:
#         for i in range(len(x)):
#             if x[i] != y[i]:
#                 return True
#     return False

def main():
    n = random.randint(N_ELEMS_MIN, N_ELEMS_MAX)
    print(f"array will be {n} elements long.")
    db = [random.randint(0, 512) for _ in range(n)]
    sorted_db = mergesort(db)

    if foundMismatches(sorted_db, sorted(db)):
        print(f"FAIL. Mismatches found between the two arrays.")
    else:
        print(f"PASS. No mismatches found between the two arrays.")

if __name__=='__main__':
    main()
