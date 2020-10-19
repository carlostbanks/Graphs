



def earliest_ancestor(ancestors, starting_node):
    ancestors_graph = Graph()
    for pair in ancestors:
        ancestors_graph.add_vertex(pair[0])
        ancestors_graph.add_vertex(pair[1])
        ancestors_graph.add_edge(pair[1], pair[0]) #bfs storing the path of how you get to the first instance of the earliest ancestor
    queue = Queue()
    queue.enqueue([starting_node])
    max_path_length = 1
    earliest = -1

    while queue.size() > 0:
        v = queue.dequeue()
        curr = v[-1]

        if len(v) > max_path_length:
            max_path_length = len(v)
            earliest = curr
        elif len(v) ==  max_path_length:
            if curr < earliest:
                earliest = curr

        for neighbor in ancestors_graph.get_neighbors(curr):
            queue.enqueue(v + [neighbor])

    return earliest