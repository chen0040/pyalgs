from pyalgs.data_structures.graphs.graph import Graph, Digraph


def create_graph():
    g = Graph(6)
    g.add_edge(0, 5)
    g.add_edge(2, 4)
    g.add_edge(2, 3)
    g.add_edge(1, 2)
    g.add_edge(0, 1)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(0, 2)

    return g


def create_graph_4_connected_components():
    g = Graph(13)
    g.add_edge(0, 5)
    g.add_edge(4, 3)
    g.add_edge(0, 1)
    g.add_edge(9, 12)
    g.add_edge(6, 4)
    g.add_edge(5, 4)
    g.add_edge(0, 2)
    g.add_edge(11, 12)
    g.add_edge(9, 10)
    g.add_edge(0, 6)
    g.add_edge(7, 8)
    g.add_edge(9, 11)
    g.add_edge(5, 3)
    return g
   

def create_digraph():
    g = Digraph(13)
    g.add_edge(4,  2)
    g.add_edge(2,  3)
    g.add_edge(3,  2)
    g.add_edge(6,  0)
    g.add_edge(0,  1)
    g.add_edge(2,  0)
    g.add_edge(11, 12)
    g.add_edge(12,  9)
    g.add_edge(9, 10)
    g.add_edge(9, 11)
    g.add_edge(7,  9)
    g.add_edge(10, 12)
    g.add_edge(11,  4)
    g.add_edge(4,  3)
    g.add_edge(3,  5)
    g.add_edge(6,  8)
    g.add_edge(8,  6)
    g.add_edge(5,  4)
    g.add_edge(0,  5)
    g.add_edge(6,  4)
    g.add_edge(6,  9)
    g.add_edge(7,  6)
    
    return g
   