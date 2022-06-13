from utils import readFile, displayWeightedGraph
from utils_kruskals import retUndirectedWeightedGraph, mstKruskals
from collections import defaultdict
import math

DATA_FILE="data/mst_data.test1.txt"

"""
    4
 1-----2
 |    /| \1
 |   / |  \
2| 3/ 5|   5
 | /   |  /
 |/    | /7
 3-----4
    6
------------
     
 1     2
 |    /| \1
 |   / |  \
2| 3/ 5|   5
 | /   |   
 |/    |  
 3     4
     
"""

def retKruskalsMST(graph):
    return mstKruskals(graph)

def main():
    edgesRawData = readFile(DATA_FILE)
    graph = retUndirectedWeightedGraph(edgesRawData)
    print(f"All of the graph's edges are as follows:")
    displayWeightedGraph(graph)

    mst = retKruskalsMST(graph)
    print(f"The Minimum Spanning Tree of this graph is:")
    displayWeightedGraph(mst)

if __name__=='__main__':
    main()
