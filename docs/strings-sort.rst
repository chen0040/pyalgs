String Sorting
==============

LSD Radix Sort
--------------

.. code-block:: python

    from pyalgs.algorithms.strings.sorting import LSD
    LSD.sort(['good', 'cool', 'done', 'come'])

MSD Radix Sort
--------------

.. code-block:: python

    from pyalgs.algorithms.strings.sorting import MSD
    words = 'more details are provided in the docs for implementation, complexities and further info'.split(' ')
    print(words)
    MSD.sort(words)
    print(words)


Sort (3-Ways String Quick Sort)
-------------------------------

.. code-block:: python

    from pyalgs.algorithms.strings.sorting import String3WayQuickSort
    words = 'more details are provided in the docs for implementation, complexities and further info'.split(' ')
    print(words)
    String3WayQuickSort.sort(words)
    print(words)


