from collections import defaultdict
from random import randint

def dfsPath(graph, s):
    explored = set()
    explored.add(s)

    search_stack = []
    search_stack.append(s)

    dist = defaultdict(int)
    dist[s] = 0

    paths = defaultdict(list)
    paths[s].append(s)

    while search_stack:
        v = search_stack.pop()
        for neighbour in graph[v]:
            if not neighbour in explored:
                dist[neighbour] = dist[v] + 1
                paths[neighbour] = paths[v][:]
                paths[neighbour].append(neighbour)

                explored.add(neighbour)
                search_stack.append(neighbour)
    return (list(explored), dist, paths)

def genRandomUndirectedGraph(n_nodes, n_edges):
    g = defaultdict(set)
    
    for i in range(n_edges):
        # Creating edge number i
        a = randint(1, n_nodes)
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

def main():
    starting_vertex = 1
    N_NODES = 15
    MAX_EDGES = maxEdgesGivenNVertices(N_NODES)
    N_EDGES = randint(N_NODES, MAX_EDGES)
    print(f"Number of nodes: {N_NODES}")
    print(f"Number of edges: {N_EDGES}")
    print(f"The maximum number of edges you could have in a graph that has \
{N_NODES} nodes is {MAX_EDGES}")
    graph = genRandomUndirectedGraph(N_NODES, N_EDGES)

    displayGraph(graph)
    (reachableNodes, dist, paths) = dfsPath(graph, starting_vertex)
    print(f"Nodes reachable by node {starting_vertex}: {reachableNodes}")
    for f in reachableNodes:
        pathToF = paths[f]
        print(f"A path from {starting_vertex} -> {f} is: {pathToF}. Distance: {dist[f]}")

main()
