from utils import readFile, displayGraph
from utils_cc import retUndirectedGraph, bfsCC
import math
from collections import defaultdict, deque

DATA_FILE="data/cc_data.test1.txt"

"""
1----4
|    |
7----|    2----|
|         |    |
9----6----8----5
|    |
3----|
--
1----4
|    |
7----|    2----|
          |    |
9----6    8----5
|    |
3----|
"""

def detNumCCs(graph):
    return bfsCC(graph)

def main():
    edgesRawData = readFile(DATA_FILE)
    graph = retUndirectedGraph(edgesRawData)
    displayGraph(graph)
    print(f"There are {bfsCC(graph)} connected components in our graph.")

if __name__=='__main__':
    main()
