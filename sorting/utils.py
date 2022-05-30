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
