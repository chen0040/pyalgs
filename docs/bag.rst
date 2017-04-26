Bag
====

.. code-block:: python

    from pyalgs.data_structures.commons.bag import Bag

    bag = Bag.create()

    bag.add(10)
    bag.add(20)
    bag.add(30)

    print [i for i in bag.iterate()]

    print bag.size()
    print bag.is_empty()

