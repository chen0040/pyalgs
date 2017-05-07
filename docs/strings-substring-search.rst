Substring Search
================


Substring Search (Brute force)
------------------------------

.. code-block:: python

    from pyalgs.algorithms.strings.substring_search import BruteForceSubstringSearch
    ss = BruteForceSubstringSearch('find')
    print(ss.search_in('I can find it here'))
    print(ss.search_in('It is not here'))


Substring Search (Rabin Karp)
-----------------------------

.. code-block:: python

    from pyalgs.algorithms.strings.substring_search import RabinKarp
    ss = RabinKarp('find')
    print(ss.search_in('I can find it here'))
    print(ss.search_in('It is not here'))

