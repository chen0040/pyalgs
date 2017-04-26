Stack
=====

.. code-block:: python

    from pyalgs.data_structures.commons.stack import Stack

    stack = Stack.create()
    stack.push(10)
    stack.push(1)

    print [i for i in stack.iterate()]

    print stack.is_empty()
    print stack.size()

    popped_item = stack.pop()
    print popped_item


