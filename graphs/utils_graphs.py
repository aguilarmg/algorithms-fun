import math
from random import random

class Vertex:
    def __init__(self, v):
        self.inNeighbours = []
        self.outNeighbours = []
        self.value = v

        self.inTime = None
        self.outTime = None
        self.status = "unvisited"
        self.parent = None
        self.estD = math.inf
        self.f_time = math.inf

    def hasOutNeighbour(self, v):
        if v in self.outNeighbours:
            return True
        return False

    def hasInNeighbour(self, v):
        if v in self.inNeighbours:
            return True
        return False

    def hasNeighbour(self, v):
        if v in self.inNeighbours or v in self.outNeighbours:
            return True
        return False

    def getOutNeighbors(self):
        return self.outNeighbours

    def getInNeighbors(self):
        return self.inNeighbours

    def addOutNeighbour(self, v):
        self.outNeighbours.append(v)

    def addInNeighbour(self, v):
        self.inNeighbours.append(v)

    def __str__(self):
        return str(self.value)

# This is a directed graph class.
# It can be used as an undirected graph by adding edges in both directions.
class Graph:
    def __init__(self):
        self.vertices = []

    def addVertex(self, n):
        self.vertices.append(n)

    # Add directed edge from u -> v
    def addDiEdge(self, u, v):
        u.addOutNeighbour(v)
        v.addInNeighbour(u)

    # Add edges in both directions from u <-> v
    def addBiEdge(self, u, v):
        self.addDiEdge(u,v)
        self.addDiEdge(v,u)

    # Reverse the edge between u and v.
    def reverseEdge(self, u, v):
        if u.hasOutNeighbour(v) and v.hasInNeighbour(u):
            if v.hasOutNeighbour(u) and u.hasInNeighbour(v):
                return
            self.addDiEdge(v,u)
            u.outNeighbours.remove(v)
            v.inNeighbours.remove(u)

    # Get a list of all the directed edges.
    def getDirEdges(self):
        ret = []
        for v in self.vertices:
            ret += [ [v,w] for w in v.outNeighbours ]
        return ret

    def __str__(self):
        ret = "Graph with:\n"
        ret += "\t Vertices:\n\t"
        for v in self.vertices:
            ret += str(v) + ","
        ret += "\n"
        ret += "\t Edges:\n\t"
        for a,b in self.getDirEdges():
            ret += "(" + str(a) + "," + str(b) + ") "
        ret += "\n"
        return ret


# Make a random graph.
# This is G(n,p), where graph has n vertices and each directed edge is present
# with probability p.
def randomGraph(n, p):
    G = Graph()
    V = [ Vertex(x) for x in range(n) ]
    for v in V:
        G.addVertex(v)

    for v in V:
        for w in V:
            if v != w:
                if random() < p:
                    G.addDiEdge(v,w)

    return G


