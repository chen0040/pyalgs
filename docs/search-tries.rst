Search Tries
============

Symbol Table using R-ways Search Tries
--------------------------------------

.. code-block:: python

    from pyalgs.data_structures.strings.search_tries import RWaySearchTries
    st = RWaySearchTries()

    st.put("one", 1)
    st.put("two", 2)
    st.put("three", 3)
    st.put("six", 6)
    st.put("ten", 10)

    for key in st.keys():
        print(key)

    print st.get("one"))
    print st.contains_key("two")

    print st.size()
    print st.is_empty()

    st.delete("one")

    for key in st.keys_with_prefix('t'):
        print(key)


Symbol Table using Ternary Search Tries
---------------------------------------


.. code-block:: python

    from pyalgs.data_structures.strings.search_tries import TernarySearchTries
    st = TernarySearchTries()

    st.put("one", 1)
    st.put("two", 2)
    st.put("three", 3)
    st.put("six", 6)
    st.put("ten", 10)

    for key in st.keys():
        print(key)

    print st.get("one"))
    print st.contains_key("two")

    print st.size()
    print st.is_empty()

    st.delete("one")

    for key in st.keys_with_prefix('t'):
        print(key)

