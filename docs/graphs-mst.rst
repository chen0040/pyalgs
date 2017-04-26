Minimum Spanning Tree
=====================

Minimum Spanning Tree (Kruskal)
-------------------------------

.. code-block:: python

    g = create_edge_weighted_graph()
    mst = KruskalMST(g)

    tree = mst.spanning_tree()

    for e in tree:
        print(e)