from utils_graphs import *

def dfsTopo(G, s, curLabel):
    s.status = "visited"
    for neighbour in s.outNeighbours:
        if neighbour.status == "unvisited":
            curLabel = dfsTopo(G, neighbour, curLabel)
    s.f_time = curLabel
    curLabel -= 1
    return curLabel

def topoSort(G):
    for v in G.vertices:
        v.status = "unvisited"

    curLabel = len(G.vertices)

    for v in G.vertices:
        if v.status == "unvisited":
            dfsTopo(G, v, curLabel)

    for v in G.vertices:
        print(f"f({v}): {v.f_time}")

def main():
    G = Graph()
    s = Vertex("s")
    v = Vertex("v")
    w = Vertex("w")
    t = Vertex("t")

    G.addVertex(s)
    G.addVertex(v)
    G.addVertex(w)
    G.addVertex(t)

    G.addDiEdge(s, v)
    G.addDiEdge(s, w)
    G.addDiEdge(v, t)
    G.addDiEdge(w, t)

    print(f"{G}")

    f_values = topoSort(G)

if __name__=='__main__':
    main()
