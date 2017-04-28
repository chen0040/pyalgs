Shortest Path
=============

Dijkstra
--------

.. code-block:: python

    from pyalgs.algorithms.graphs.shortest_path import DijkstraShortestPath
    g = create_edge_weighted_digraph()
    s = 0
    dijkstra = DijkstraShortestPath(g, s)
    for v in range(1, g.vertex_count()):
        if dijkstra.hasPathTo(v):
            print(str(s) + ' is connected to ' + str(v))
            print('path is ' + ' .. '.join([str(i) for i in dijkstra.shortestPathTo(v)]))
            print('path length is ' + str(dijkstra.path_length_to(v)))


Shortest Path (Topological Sort)
--------------------------------

.. code-block:: python

    from pyalgs.algorithms.graphs.shortest_path import TopologicalSortShortestPath
    g = create_edge_weighted_digraph()
    assert not DirectedCycle(g).hasCycle()
    s = 0
    dijkstra = TopologicalSortShortestPath(g, s)
    for v in range(1, g.vertex_count()):
        if dijkstra.hasPathTo(v):
            print(str(s) + ' is connected to ' + str(v))
            print('shortest path is ' + ' .. '.join([str(i) for i in dijkstra.shortestPathTo(v)]))
            print('path length is ' + str(dijkstra.path_length_to(v)))

