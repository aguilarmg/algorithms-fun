from collections import defaultdict, deque

def retUndirectedGraph(data):
    graph = defaultdict(list)
    for line in data:
        edge = line.split() 
        # After calling split() on the line, `edgeStr` should be in the 
        # format [ tail, head ], where tail and head are strings
        v = int(edge[0]) 
        w = int(edge[1])
        if (w not in graph[v]) and (v not in graph[w]):
            graph[v].append(w)
            graph[w].append(v)

    return graph

def bfs(graph, s, explored):
    queue = deque()
    queue.append(s)

    explored.add(s)

    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in explored:
                queue.append(w)
                explored.add(w)

    return list(explored)

def bfsCC(graph):
    explored = set()
    nCC = 0

    for vertex in graph.keys():
        if vertex not in explored:
            nCC += 1
            bfs(graph, vertex, explored)
    return nCC
