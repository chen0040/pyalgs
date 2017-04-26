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

    from pyalgs.data_structures.graphs.graph import EdgeWeightGraph
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
