from pyalgs.data_structures.graphs.graph import Graph, Digraph, EdgeWeightedGraph, Edge


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
    g.add_edge(4, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 2)
    g.add_edge(6, 0)
    g.add_edge(0, 1)
    g.add_edge(2, 0)
    g.add_edge(11, 12)
    g.add_edge(12, 9)
    g.add_edge(9, 10)
    g.add_edge(9, 11)
    g.add_edge(7, 9)
    g.add_edge(10, 12)
    g.add_edge(11, 4)
    g.add_edge(4, 3)
    g.add_edge(3, 5)
    g.add_edge(6, 8)
    g.add_edge(8, 6)
    g.add_edge(5, 4)
    g.add_edge(0, 5)
    g.add_edge(6, 4)
    g.add_edge(6, 9)
    g.add_edge(7, 6)

    return g


def create_dag():
    dag = Digraph(7)

    dag.add_edge(0, 5)
    dag.add_edge(0, 2)
    dag.add_edge(0, 1)
    dag.add_edge(3, 6)
    dag.add_edge(3, 5)
    dag.add_edge(3, 4)
    dag.add_edge(5, 4)
    dag.add_edge(6, 4)
    dag.add_edge(6, 0)
    dag.add_edge(3, 2)
    dag.add_edge(1, 4)

    return dag


def create_edge_weighted_graph():
    g = EdgeWeightedGraph(8)
    g.add_edge(Edge(0, 7, 0.16))
    g.add_edge(Edge(2, 3, 0.17))
    g.add_edge(Edge(1, 7, 0.19))
    g.add_edge(Edge(0, 2, 0.26))
    g.add_edge(Edge(5, 7, 0.28))
    g.add_edge(Edge(1, 3, 0.29))
    g.add_edge(Edge(1, 5, 0.32))
    g.add_edge(Edge(2, 7, 0.34))
    g.add_edge(Edge(4, 5, 0.35))
    g.add_edge(Edge(1, 2, 0.36))
    g.add_edge(Edge(4, 7, 0.37))
    g.add_edge(Edge(0, 4, 0.38))
    g.add_edge(Edge(6, 2, 0.4))
    g.add_edge(Edge(3, 6, 0.52))
    g.add_edge(Edge(6, 0, 0.58))
    g.add_edge(Edge(6, 4, 0.93))

    return g
