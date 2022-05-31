from random import randint

def foundMismatches(x, y):
    if len(x) != len(y):
        return True
    else:
        for i in range(len(x)):
            if x[i] != y[i]:
                return True
    return False

def testForMismatches(x, y):
    if foundMismatches(x,y):
        print(f"FAIL. Mismatches found between the two arrays.")
    else:
        print(f"PASS. No mismatches found between the two arrays.")

def genRandomIntArray(n_elems_min, n_elems_max):
    n = randint(n_elems_min, n_elems_max)
    print(f"array will be {n} elements long.")
    return [randint(0, 512) for _ in range(n)]
