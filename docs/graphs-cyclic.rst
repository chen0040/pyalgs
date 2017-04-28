Cyclic Graph Detection
======================

Directed Cycle Detection
------------------------

.. code-block:: python

    from pyalgs.algorithms.graphs.directed_cycle import DirectedCycle
    dag = create_dag()
        dc = DirectedCycle(dag)
        assertFalse(dc.hasCycle())

