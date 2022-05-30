from collections import defaultdict
import math
import time
import heapq

class Edge:
    
    # Constructor
    def __init__(self, tail, head, weight):
        self.tail = tail
        self.head = head
        self.weight = weight

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def getWeight(self):
        return self.weight

    def __str__(self):
        return f"{self.tail} -> {self.head} ({self.weight})"

    def __repr__(self):
        return f"{self.tail} -> {self.head} ({self.weight})"

    def __lt__(self, obj):
        return self.weight < obj.weight


def initGraph():
    graph = defaultdict(lambda: defaultdict(int))
    edges = []

    graph["s"]["v"] = 1
    graph["s"]["w"] = 4
    edges.append(Edge("s","v", 1))
    edges.append(Edge("s","w", 4))

    graph["v"]["w"] = 2
    graph["v"]["t"] = 6
    edges.append(Edge("v","w", 2))
    edges.append(Edge("v","t", 6))

    graph["w"]["t"] = 3
    edges.append(Edge("w","t", 3))

    graph["t"] = defaultdict(int)

    heapq.heapify(edges)

    return (graph, edges)

def initCosts(graph, s):
    inf = math.inf
    dist = defaultdict(int)

    # Initialise cost to get from vertex s to vertex s as 0
    # Initialise cost to get from s to v, where v != s, as +inf
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

def findCheapestEdge(edges):
    return heapq.heappop(edges)

def dijkstra(graph, edges, s):
    costs = initCosts(graph, s)
    X = []
    X.append(s)

    while checkForEdgeCrossingFrontier(graph, X):
        cheapestEdge = findCheapestEdge(edges)
        # print(f"The cheapest edge found in the graph was: {cheapestEdge}")
        v = cheapestEdge.getTail()
        w = cheapestEdge.getHead()
        l_vw = cheapestEdge.getWeight()
        X.append(w)
        costs[w] = costs[v] + l_vw

    return costs   

def main():
    starting_vertex= "s"
    (graph, edges) = initGraph()
    print(f"Graph")
    for v,neighbours in sorted(graph.items()):
        for neighbour, weight in sorted(neighbours.items()):
            print(f"{v} -> {neighbour} ({weight})")

    print(f"Edges")
    for edge in edges:
        print(edge)
    
    print(f"Going to begin timing the simple implementation of Dijkstra's")
    start = time.time()
    costs = dijkstra(graph, edges, starting_vertex)
    end = time.time()

    print(f"dist(s,*) from starting vertex {starting_vertex} to all other \
vertices: \n{costs}")
    print(f"Time taken: {end-start}")
main()
