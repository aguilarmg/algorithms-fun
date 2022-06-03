from utils import *
from random import randint, seed
from collections import deque, defaultdict
import math

def bfs(graph, s, getDist=False, getPaths=False):
    """
    Input:
    - Graph
    - Source vertex

    Output:
    - All reachable nodes from source vertex
    - Distance to all nodes.
        - dist[w] = distance from s->w if w is reachable from s
    """
    explored = set()
    explored.add(s)

    search_queue = deque()
    search_queue.append(s)

    if getDist:
        dist = {}
        dist[s] = 0

    if getPaths:
        paths = defaultdict(list)
        paths[s] = [s]

    while search_queue:
        v = search_queue.popleft()

        for neighbour in graph[v]:
            if not neighbour in explored:
                explored.add(neighbour)
                search_queue.append(neighbour)
                if getDist:
                    dist[neighbour] = dist[v] + 1
                if getPaths:
                    path_to_neighbour = paths[v][:]
                    path_to_neighbour.append(neighbour)
                    paths[neighbour] = path_to_neighbour

    ret = (list(explored),)

    if getDist:
        ret = (*ret, dist)

    if getPaths:
        ret = (*ret, paths)

    return ret


def main():
    starting_vertex = 1
    N_NODES = 45
    MAX_EDGES = maxEdgesGivenNVertices(N_NODES)
    seed(MAX_EDGES+1) 
    N_EDGES = randint(N_NODES, MAX_EDGES)

    print(f"Number of nodes: {N_NODES}")
    print(f"Number of edges: {N_EDGES}")
    print(f"The maximum number of edges you could have in a graph that has \
{N_NODES} nodes is {MAX_EDGES}")
    graph = genRandomUndirectedGraph(N_NODES, N_EDGES)

    displayGraph(graph)

    (reachableNodes, distToNodes, pathsToNodes) = bfs(graph, starting_vertex, getDist=True, getPaths=True)

    print(f"The nodes reachable from {starting_vertex} are:")
    for node in reachableNodes:
        print(f"{node} ({distToNodes[node]}): {pathsToNodes[node]}")


if __name__=='__main__':
    main()
