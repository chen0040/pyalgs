Max-Flow-Min-Cut
================

MaxFlow MinCut (Ford-Fulkerson)
-------------------------------

.. code-block:: python

    from pyalgs.algorithms.graphs.max_flow import FordFulkersonMaxFlow
    network = create_flow_network()
    ff = FordFulkersonMaxFlow(network, 0, 7)
    print('max-flow: '+str(ff.max_flow_value()))

