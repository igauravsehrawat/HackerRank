def centrality_max(G, v):
    # your code here
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[v]+1
                open_list.append(neighbor)

    return (sum(distance_from_start.values())+0.0)/len(distance_from_start)
