Sorting
=======

The sorting algorithms sort an array in ascending order

Selection Sort
--------------

.. code-block:: python

    from pyalgs.algorithms.commons.sorting import SelectionSort

    a = [4, 2, 1]
    SelectionSort.sort(a)
    print(a)


Insertion Sort
--------------

.. code-block:: python

    from pyalgs.algorithms.commons.sorting import InsertionSort

    a = [4, 2, 1]
    InsertionSort.sort(a)
    print(a)


Shell Sort
----------

.. code-block:: python

    from pyalgs.algorithms.commons.sorting import ShellSort

    a = [4, 2, 1, 23, 4, 5, 6, 7, 8, 9, 20, 11, 13, 34, 66]
    ShellSort.sort(a)
    print(a)


Merge Sort
----------

.. code-block:: python

    from pyalgs.algorithms.commons.sorting import MergeSort

    a = [4, 2, 1, 23, 4, 5, 6, 7, 8, 9, 20, 11, 13, 34, 66]
    MergeSort.sort(a)
    print(a)


Quick Sort
----------

.. code-block:: python

    from pyalgs.algorithms.commons.sorting import QuickSort

    a = [4, 2, 1, 23, 4, 5, 6, 7, 8, 9, 20, 11, 13, 34, 66]
    QuickSort.sort(a)
    print(a)


3-Ways Quick Sort
-----------------

.. code-block:: python

    from pyalgs.algorithms.commons.sorting import ThreeWayQuickSort

    a = [4, 2, 1, 23, 4, 5, 6, 7, 8, 9, 20, 11, 13, 34, 66]
    ThreeWayQuickSort.sort(a)
    print(a)


Heap Sort
---------

.. code-block:: python

    from pyalgs.algorithms.commons.sorting import HeapSort

    a = [4, 2, 1, 23, 4, 5, 6, 7, 8, 9, 20, 11, 13, 34, 66]
    HeapSort.sort(a)
    print(a)



