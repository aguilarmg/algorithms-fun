def readFile(fname):
    ret = []
    f = open(fname, 'r')
    line = f.readline()
    while (line):
        ret.append(line)
        line = f.readline()
    return ret
