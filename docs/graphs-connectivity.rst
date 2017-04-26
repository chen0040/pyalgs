Graph Connectivity
==================

Connected Components for undirected graph
-----------------------------------------

.. code-block:: python

    from pyalgs.algorithms.graphs.connectivity import ConnectedComponents
    G = create_graph()

    cc = ConnectedComponents(G)
    print('connected component count: ' + str(cc.count()))


    for v in range(G.vertex_count()):
        print('id[' + str(v) + ']: ' + str(cc.id(v)))
    for v in range(G.vertex_count()):
        r = randint(0, G.vertex_count()-1)
        if cc.connected(v, r):
            print(str(v) + ' is connected to ' + str(r))