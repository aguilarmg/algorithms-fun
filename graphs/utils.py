from collections import defaultdict
from random import randint, seed

def genRandomUndirectedGraph(n_nodes, n_edges):
    g = defaultdict(set)
    
    for i in range(n_edges):
        # Creating edge number i
        seed(i*n_nodes)
        a = randint(1, n_nodes)
        seed((i+1)*n_nodes + 1)
        b = randint(1, n_nodes)
        # Attempting to create a node from a <-> b. 
        # Must perform checks to see if it's possible.
        while a == b or b in g[a]:
            # Don't create an edge from a node to itself.
            # Don't create an edge if it already exists.

            # If deg(a) == n_nodes-1, then reroll node a.
            if len(g[a]) == n_nodes-1:
                a = randint(1, n_nodes)
                continue

            # Reroll node b, and perform checks on edge a <-> b.
            b = randint(1, n_nodes)
        g[a].add(b)
        g[b].add(a)

    return g

def maxEdgesGivenNVertices(n):
    # Base case
    if n < 2:
        return 0
    elif n == 2:
        return 1
    else:
        return maxEdgesGivenNVertices(n-1) + (n-1)

def displayGraph(g):
    for v in sorted(g.keys()):
        print(f"{v}: {g[v]}")

def displayWeightedGraph(g):
    for u in sorted(g.keys()):
        for v in sorted(g[u].keys()):
            print(f"{u} -> {v} ({g[u][v]})")

def readFile(fname):
    ret = []

    f = open(fname, 'r') 
    line = f.readline()
    while (line):
        ret.append(line)
        line = f.readline()
    return ret
