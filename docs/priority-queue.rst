Priority Queue
==============

Minimum Priority Queue
----------------------

.. code-block:: python

    from pyalgs.data_structures.commons.priority_queue import MinPQ

    pq = MinPQ.create()
    pq.enqueue(10)
    pq.enqueue(5)
    pq.enqueue(12)
    pq.enqueue(14)
    pq.enqueue(2)

    print pq.is_empty()
    print pq.size()

    print [i for i in pq.iterate()]

    deleted = pq.del_min()
    print(deleted)


Maximum Priority Queue
----------------------


.. code-block:: python

    from pyalgs.data_structures.commons.priority_queue import MaxPQ

    pq = MaxPQ.create()
    pq.enqueue(10)
    pq.enqueue(5)
    pq.enqueue(12)
    pq.enqueue(14)
    pq.enqueue(2)

    print pq.is_empty()
    print pq.size()

    print [i for i in pq.iterate()]

    deleted = pq.del_max()
    print deleted

