Topological Sort
================

.. code-block:: python

    from pyalgs.algorithms.graphs.topological_sort import DepthFirstOrder
    G = create_graph()
    topological_sort = DepthFirstOrder(G)
    print(' => '.join([str(i) for i in topological_sort.postOrder()]))