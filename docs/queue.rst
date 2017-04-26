Queue
=====

.. code-block:: python

    from pyalgs.data_structures.commons.queue import Queue

    queue = Queue.create()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print [i for i in queue.iterate()]

    print queue.size()
    print queue.is_empty()

    deleted_item = queue.dequeue())
    print deleted_item


