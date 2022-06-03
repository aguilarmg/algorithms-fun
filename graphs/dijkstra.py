from collections import defaultdict
import math
import time

def initGraph():
    graph = defaultdict(lambda: defaultdict(int))

    graph["s"]["v"] = 1
    graph["s"]["w"] = 4
    
    graph["v"]["w"] = 2
    graph["v"]["t"] = 6

    graph["w"]["t"] = 3

    graph["t"] = defaultdict(int)

    return graph

def initCosts(graph, s):
    inf = math.inf
    dist = defaultdict(int)

    # Initialise cost to get from vertex s to vertex s as 0.
    # Initialise cost to get from s to v, where v != s, as +inf.
    dist[s] = 0
    for v in graph.keys():
        if v != s:
            dist[v] = inf

    return dist

def checkForEdgeCrossingFrontier(graph, X):
    for v in X:
        for w in graph[v]:
            if w not in X:
                # print(f"The edge from {v} -> {w} has not been explored. This edge crosses the frontier from X to V-X.")
                return True
    return False

def findCheapestEdge(graph, X):
    minEdgeWeight = math.inf
    minEdgeHead = None
    minEdgeTail = None
    for v in X:
        for w in graph[v]:
            if graph[v][w] < minEdgeWeight and w not in X:
                minEdgeWeight = graph[v][w]
                minEdgeTail = v
                minEdgeHead = w

    return (minEdgeTail, minEdgeHead)


def dijkstra(graph, s):
    costs = initCosts(graph, s)
    X = []
    X.append(s)

    while checkForEdgeCrossingFrontier(graph, X):
        (v,w) = findCheapestEdge(graph, X)
        # print(f"The cheapest edge was from {v} -> {w}")
        X.append(w)
        costs[w] = costs[v] + graph[v][w]

    return costs

def main():
    starting_vertex = "s" 
    graph = initGraph()
    print(f"Graph")
    for v,neighbours in sorted(graph.items()):
        for neighbour, weight in sorted(neighbours.items()):
            print(f"{v} -> {neighbour} ({weight})")

    print(f"Going to begin timing the simple implementation of Dijkstra's")
    start = time.time()
    costs = dijkstra(graph, starting_vertex)
    end = time.time()
    print(f"dist(s,*) from starting vertex {starting_vertex} to all other \
vertices: \n{costs}")
    print(f"Time taken: {end-start}")

main()
