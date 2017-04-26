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
