from utils import readFile
from utils_wis import genPathGraph, calcMwisValue, reconstructMWIS

# DATA_FILE='data/wis_00.txt'
DATA_FILE='data/wis_01.txt'

def main():
    wis_rawdata = readFile(DATA_FILE)
    path_graph = genPathGraph(wis_rawdata)
    
    n = len(path_graph)
    opt_values = [None]*(n)
    
    mwis_value = calcMwisValue(path_graph, opt_values, n-1)
    print(f"The total value of the MWIS for this path graph is: {mwis_value}")
    mwis = reconstructMWIS(path_graph, opt_values, n-1)
    print(f"the MWIS of this path graph is: {mwis}")

if __name__=='__main__':
    main()
