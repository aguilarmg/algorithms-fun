from utils_knapsack import Item

def initItems():
    ret = []
    ret.append(Item(3,4))
    ret.append(Item(2,3))
    ret.append(Item(4,2))
    ret.append(Item(4,3))

    return ret

def getDpArr(items, C):
    n = len(items)
    print(f"There are {n} items.")
    print(f"The capacity is {C}.")

    # Construct your 2D array.
    A = [[0 for c in range(C+1)] for i in range(n+1)]

    for i in range(n):
        for c in range(C+1):
            s_i = items[i].size
            v_i = items[i].value

            if s_i > c:
                A[i+1][c] = A[i][c]
            else:
                A[i+1][c] = max(A[i][c], A[i][c-s_i] + v_i)

    for i in range(len(A)):
        print(f"{A[i]}")

    return A

def reconstruct(A, items, C):
    S = []
    n = len(items)
    c = C
    for i in reversed(range(1,n+1)):
        s_i = items[i-1].size
        v_i = items[i-1].value
        if s_i <= c and (A[i][c-s_i]+v_i) >= A[i][c]:
            S.append(items[i-1])
            c -= s_i
    return S

def main():
    items = initItems()
    n = len(items)
    C = 6
    for (i,item) in enumerate(items):
        if not item:
            print(f"{item}")
            continue
        print(f"Item {i}: {item}")

    dpArr = getDpArr(items, C)
    print(f"Optimal solution value: {dpArr[n][C]}")

    solution = reconstruct(dpArr, items, C)
    for item in solution:
        print(f"{item}")

if __name__=='__main__':
    main()
