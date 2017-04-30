from pyalgs.data_structures.graphs.graph import Graph, Digraph, EdgeWeightedGraph, Edge, EdgeWeightedGraph, \
    DirectedEdgeWeightedGraph, FlowNetwork, FlowEdge


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


def create_edge_weighted_digraph():
    g = DirectedEdgeWeightedGraph(8)

    g.add_edge(
        Edge(0, 1, 5.0))
    g.add_edge(
        Edge(0, 4, 9.0))
    g.add_edge(
        Edge(0, 7, 8.0))
    g.add_edge(
        Edge(1, 2, 12.0))
    g.add_edge(
        Edge(1, 3, 15.0))
    g.add_edge(
        Edge(1, 7, 4.0))
    g.add_edge(
        Edge(2, 3, 3.0))
    g.add_edge(
        Edge(2, 6, 11.0))
    g.add_edge(
        Edge(3, 6, 9.0))
    g.add_edge(
        Edge(4, 5, 5.0))
    g.add_edge(
        Edge(4, 6, 20.0))
    g.add_edge(
        Edge(4, 7, 5.0))
    g.add_edge(
        Edge(5, 2, 1.0))
    g.add_edge(
        Edge(5, 6, 13.0))
    g.add_edge(
        Edge(7, 5, 6.0))
    g.add_edge(
        Edge(7, 2, 7.0))

    return g


def create_digraph_4_strongly_connected_components():
    graph = Digraph(13)
    graph.add_edge(4, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 2)
    graph.add_edge(6, 0)
    graph.add_edge(0, 1)
    graph.add_edge(2, 0)
    graph.add_edge(11, 12)
    graph.add_edge(12, 9)
    graph.add_edge(9, 10)
    graph.add_edge(9, 11)
    graph.add_edge(8, 9)
    graph.add_edge(10, 12)
    graph.add_edge(11, 4)
    graph.add_edge(4, 3)
    graph.add_edge(3, 5)
    graph.add_edge(7, 8)
    graph.add_edge(8, 7)
    graph.add_edge(5, 4)
    graph.add_edge(0, 5)
    graph.add_edge(6, 4)
    graph.add_edge(6, 9)
    graph.add_edge(7, 6)

    return graph


def create_flow_network():
    g = FlowNetwork(8)
    g.add_edge(FlowEdge(0, 1, 10))
    g.add_edge(FlowEdge(0, 2, 5))
    g.add_edge(FlowEdge(0, 3, 15))
    g.add_edge(FlowEdge(1, 4, 9))
    g.add_edge(FlowEdge(1, 5, 15))
    g.add_edge(FlowEdge(1, 2, 4))
    g.add_edge(FlowEdge(2, 5, 8))
    g.add_edge(FlowEdge(2, 3, 4))
    g.add_edge(FlowEdge(3, 6, 16))
    g.add_edge(FlowEdge(4, 5, 15))
    g.add_edge(FlowEdge(4, 7, 10))
    g.add_edge(FlowEdge(5, 7, 10))
    g.add_edge(FlowEdge(5, 6, 15))
    g.add_edge(FlowEdge(6, 2, 6))
    g.add_edge(FlowEdge(6, 7, 10))

    return g
