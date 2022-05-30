def foundMismatches(x, y):
    if len(x) != len(y):
        return True
    else:
        for i in range(len(x)):
            if x[i] != y[i]:
                return True
    return False
