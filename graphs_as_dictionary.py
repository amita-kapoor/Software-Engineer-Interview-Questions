def add_node(graph, node):
    """ Adds a node to the graph represented as a dictionary
    Arguments:
    Dictionary representing the main graph, the node to be added
    Returns:
         the dictionary 'graph' after ading the node
    """
    graph[node] = []


def add_edge(graph, source, dest):
    """
    Adds an edge (present implementation undirected) between source and destination nodes. In case either source or
    destination nodes do not exist it firsts ad them in the graph
    Arguments
    :param graph: The dictionary structure representing the graph
    :param source: The source node
    :param dest: the destination node
    :return: the modified dictionary structure.
    """
    if source not in graph:
        add_node(graph,source)
    if dest not in graph:
        add_node(graph,dest)
    graph[source].append(dest)
    graph[dest].append(source)

def connected(graph, source, dest):
    """
    Tells whether node source and dest are connected or not
    :param graph:
    :param source:
    :param dest:
    :return:
    """
    if source in graph[dest] and dest in graph[source]:
        return True
    return False

def print_edges(graph):
    """
    Print all the connected edges in the graph
    :param graph: The dictionary structure representing the graph
    :return: A list edges containing all connected adges as list of tuples
    """
    edges = []
    for x in graph:
        for y in graph[x]:
            edges.append((x,y))
    return edges

def isolated(graph):
    iso = []
    for x in graph:
        if graph[x] == []:
            iso.append(x)
    return iso
graph = {}
add_node(graph, "f")
add_edge(graph,"a", "c")
add_edge(graph,"d", "c")
add_edge(graph,"b", "c")
add_edge(graph,"e", "c")
add_edge(graph,"b", "e")
print(print_edges(graph))
print(isolated(graph))
print(graph)