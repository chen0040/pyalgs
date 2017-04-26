Graph
=====

Undirected Graph
----------------

.. code-block:: python

    from pyalgs.data_structures.graphs.graph import Graph
    G = Graph(100)

    G.add_edge(1, 2)
    G.add_edge(1, 3)

    print([i for i in G.adj(1)])
    print([i for i in G.adj(2)])
    print([i for i in G.adj(3)])

    print(G.vertex_count())

Directed Graph
--------------

.. code-block:: python

    from pyalgs.data_structures.graphs.graph import Digraph
    G = Digraph(100)

    G.add_edge(1, 2)
    G.add_edge(1, 3)

    print([i for i in G.adj(1)])
    print([i for i in G.adj(2)])
    print([i for i in G.adj(3)])

    print(G.vertex_count())
