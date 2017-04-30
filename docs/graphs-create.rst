Create Graphs
=============

Create Undirected Graph
-----------------------

.. code-block:: python

    from pyalgs.data_structures.graphs.graph import Graph
    def create_graph():
        G = Graph(100)

        G.add_edge(1, 2)
        G.add_edge(1, 3)

        print([i for i in G.adj(1)])
        print([i for i in G.adj(2)])
        print([i for i in G.adj(3)])

        print(G.vertex_count())

Create Directed Graph
---------------------

.. code-block:: python

    from pyalgs.data_structures.graphs.graph import Digraph
    def create_digraph():
        G = Digraph(100)

        G.add_edge(1, 2)
        G.add_edge(1, 3)

        print([i for i in G.adj(1)])
        print([i for i in G.adj(2)])
        print([i for i in G.adj(3)])

        print(G.vertex_count())

Edge Weighted Graph
-------------------

.. code-block:: python

    from pyalgs.data_structures.graphs.graph import EdgeWeightGraph, Edge
    def create_edge_weighted_graph():
        g = EdgeWeightedGraph(8)
        g.add_edge(Edge(0, 7, 0.16))
        g.add_edge(Edge(2, 3, 0.17))
        g.add_edge(Edge(1, 7, 0.19))
        g.add_edge(Edge(0, 2, 0.26))
        g.add_edge(Edge(5, 7, 0.28))

        print([edge for edge in G.adj(3)])

        print(G.vertex_count())
        print(', '.join([edge for edge in G.edges()]))
        return g

Directed Edge Weighted Graph
----------------------------

.. code-block:: python

    from pyalgs.data_structures.graphs.graph import DirectedEdgeWeightedGraph, Edge
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
        return g


Flow Network ( for max-flow min-cut problem)
--------------------------------------------

.. code-block:: python

    from pyalgs.data_structures.graphs.graph import FlowNetwork, FlowEdge
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
