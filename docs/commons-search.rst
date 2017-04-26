Searching
=========

Binary Selection
----------------

.. code-block:: python

    from pyalgs.algorithms.commons.selecting import BinarySelection
    from pyalgs.algorithms.commons.util import is_sorted


    a = [1, 2, 13, 22, 123]
    assert is_sorted(a)
    print BinarySelection.index_of(a, 13)