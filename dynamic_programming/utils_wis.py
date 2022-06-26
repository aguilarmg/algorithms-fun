def genPathGraph(data) -> list[int]:
    """
    Data is in the form:
    [number of vertices in path graph]
    [weight of vertex 1]
    [weight of vertex 2]
    ...
    """
    n = int(data[0])
    ret = [None]*n
    for i in range(n):
        ret[i] = int(data[i+1])

    return ret

def calcMwisValue(path_graph, opt_values, i) -> int:
    """
    Only need to calculate opt_values[i] if we haven't cached it before.
    """
    if not opt_values[i]:
        """
        Build up the solution for opt_values[i] as necessary.
        """
        for j in range(i+1):
            """
            For j=0,...,i-1, we only need to calculate opt_values[j] if we
            haven't calculated and cached it before.
            """
            if not opt_values[j]:
                print(f"Haven't calced opt_values[j] for j={j} yet.")
                if j == 0:
                    opt_values[j] = path_graph[j]
                elif j == 1:
                    opt_values[j] = max(opt_values[j-1], path_graph[j])
                else: 
                    opt_values[j] = max(opt_values[j-1], opt_values[j-2]+path_graph[j])
    return opt_values[i]

def reconstructMWIS(path_graph, opt_values, i) -> list[int]:
    """
    Return a list containing the vertex indices that belong in the
    maximum-weighted independent set.
    """
    s = []
    j = i

    while j >= 1:
        if opt_values[j] == opt_values[j-1]:
            j -= 1
        else:
            s.append(j)
            j -= 2

    return s
