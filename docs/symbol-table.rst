Symbol Table
============

Symbol Table using Binary Search Tree
-------------------------------------

.. code-block:: python

    from pyalgs.data_structures.commons.binary_search_tree import BinarySearchTree
    bst = BinarySearchTree.create()

    bst.put("one", 1)
    bst.put("two", 2)
    bst.put("three", 3)
    bst.put("six", 6)
    bst.put("ten", 10)

    for key in bst.keys():
        print(key)

    print bst.get("one"))
    print bst.contains_key("two")

    print bst.size()
    print bst.is_empty()

    bst.delete("one")


Symbol Table using Left Leaning Red Black Tree
----------------------------------------------

.. code-block:: python

    from pyalgs.data_structures.commons.binary_search_tree import BinarySearchTree
    bst = BinarySearchTree.create_red_black_tree()

    bst.put("one", 1)
    bst.put("two", 2)
    bst.put("three", 3)
    bst.put("six", 6)
    bst.put("ten", 10)

    print bst.get("one"))
    print bst.contains_key("two")

    for key in bst.keys():
        print(key)

    print bst.size()
    print bst.is_empty()

    bst.delete("one")


Symbol Table using Hashed Map
-----------------------------

.. code-block:: python

    from pyalgs.data_structures.commons.hashed_map import HashedMap
    map = HashedMap.create()

    map.put("one", 1)
    map.put("two", 2)
    map.put("three", 3)
    map.put("six", 6)
    map.put("ten", 10)

    print map.get("one"))
    print map.contains_key("two")

    for key in map.keys():
        print(key)

    print map.size()
    print map.is_empty()

    map.delete("one")


Symbol Table using Hashed Set
-----------------------------

.. code-block:: python

    from pyalgs.data_structures.commons.hashed_set import HashedSet
    set = HashedSet.create()

    set.add("one")
    set.add("two")
    set.add("three")
    set.add("six")
    set.add("ten")

    print set.contains("two")

    for key in set.iterate():
        print(key)

    print set.size()
    print set.is_empty()

    set.delete("one")


