from collections import defaultdict
from heapq import heappush, heappop, heapify

class Edge():
    def __init__(self, u, v, w=None):
        self.tail = u
        self.head = v 
        self.weight = w

    def setWeight(self, w):
        self.weight = w

    def __lt__(self, x):
        return self.weight < x.weight

    def __str__(self):
        return f"{self.tail}->{self.head} ({self.weight})"

    def __repr__(self):
        return f"{self.tail}->{self.head} ({self.weight})"

def retUndirectedWeightedGraph(data):
    graph = defaultdict(lambda : defaultdict(int))

    for line in data:
        edge = line.split()
        """
        After calling split() on the line, `edge` should be in the format
        [ tail, head, weight ], where all are strings.
        """
        u = int(edge[0])
        v = int(edge[1])
        weight = int(edge[2])
        
        """
        Only add to the graph if an edge between these two nodes doesn't already
        exist.
        """
        if (v not in graph[u].keys()) and (u not in graph[v].keys()):
            graph[u][v] = weight
            graph[v][u] = weight

    return graph

def constructEdges(graph):
    ret = []
    for u in graph.keys():
        for v in graph[u].keys():
            ret.append(Edge(u,v,graph[u][v]))

    return ret

def initializeUnionFind(graph):
    parents = defaultdict(int)
    sizes = defaultdict(int)

    for v in graph.keys():
        parents[v] = v
        sizes[v] = 1

    return parents, sizes

def find(parents, x):
    if parents[x] == x:
        return x
    else:
        return find(parents, parents[x])

def union(parents, sizes, x, y):
    if sizes[x] > sizes[y]:
        parents[y] = x
        sizes[x] += sizes[y]
    else:
        parents[x] = y
        sizes[y] += sizes[x]

def mstKruskals(graph):
    T = defaultdict(lambda: defaultdict(int))

    edges = constructEdges(graph)

    """
    Create a min-heap so that you can access the edges in order of increasing
    cost.
    """
    heapify(edges)

    """
    Initialize Union-Find
    """
    parents, sizes = initializeUnionFind(graph)

    """
    Keep track of edge endpoints since (u,v) == (v,u) in an undirected graph, so
    you only need to consider the specific pair once.
    """
    exploredTuples = set()

    for _ in range(len(edges)):
        edge = heappop(edges) 
        """
        If this pair of nodes has already been considered, skip it.
        """
        if ((edge.head, edge.tail) in exploredTuples) or ((edge.tail, edge.head) in exploredTuples):
            continue


        """ 
        If the edge endpoints share the same parent, then this
        edge already exists in T.
        """
        x = find(parents, edge.tail)
        y = find(parents, edge.head)
        
        if x != y:
            """
            This edge does not exist in T, thus add it to T and update to
            indicate the component fusion.
            """
            T[edge.tail][edge.head] = edge.weight
            T[edge.head][edge.tail] = edge.weight
            union(parents, sizes, x, y)

        exploredTuples.add((edge.tail, edge.head))
    
    return T
