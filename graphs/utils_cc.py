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

def find(parents, x):
    if parents[x] == x:
        return x
    else:
        return find(parents, parents[x])

def union(parents, x, y, sizes):
    if sizes[x] > sizes[y]:
        parents[y] = x
        sizes[x] += sizes[y]
    else:
        parents[x] = y
        sizes[y] += sizes[x]

def constructEdges(graph):
    ret = []
    for v in graph.keys():
        for w in graph[v]:
            if ((w,v) not in ret) and ((v,w) not in ret):
                ret.append((v,w))
    return ret

def unionFindCCs(graph):
    V = graph.keys()
    parents = defaultdict(int)
    sizes = defaultdict(int)

    E = constructEdges(graph)
    
    # Initialize
    for v in V:
        parents[v] = v
        sizes[v] = 1
    
    for e in E:
        x = find(parents, e[0])
        y = find(parents, e[1])
        if x != y:
            union(parents, x, y, sizes)
    return len(set(parents.values()))

