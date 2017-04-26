Graph Search
============

Depth First Search
------------------

.. code-block:: python

    from pyalgs.algorithms.graphs.search import DepthFirstSearch
    g = create_graph()
    s = 0
    dfs = DepthFirstSearch(g, s)

    for v in range(1, g.vertex_count()):
        if dfs.hasPathTo(v):
            print(str(s) + ' is connected to ' + str(v))
            print('path is ' + ' => '.join([str(i) for i in dfs.pathTo(v)]))
            
Breadth First Search
------------------

.. code-block:: python

    from pyalgs.algorithms.graphs.search import BreadthFirstSearch
    g = create_graph()
    s = 0
    dfs = BreadthFirstSearch(g, s)

    for v in range(1, g.vertex_count()):
        if dfs.hasPathTo(v):
            print(str(s) + ' is connected to ' + str(v))
            print('path is ' + ' => '.join([str(i) for i in dfs.pathTo(v)]))

