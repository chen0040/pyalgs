Minimum Spanning Tree
=====================

Minimum Spanning Tree (Kruskal)
-------------------------------

.. code-block:: python

    from pyalgs.algorithms.graphs.minimum_spanning_trees import KruskalMST
    g = create_edge_weighted_graph()
    mst = KruskalMST(g)

    tree = mst.spanning_tree()

    for e in tree:
        print(e)

Minimum Spanning Tree (Lazy Prim)
---------------------------------

.. code-block:: python

    from pyalgs.algorithms.graphs.minimum_spanning_trees import LazyPrimMST
    g = create_edge_weighted_graph()
    mst = LazyPrimMST(g)

    tree = mst.spanning_tree()

    for e in tree:
        print(e)