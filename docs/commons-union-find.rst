Union Find
==========

.. code-block:: python

    from pyalgs.algorithms.commons.union_find import UnionFind

    uf = UnionFind.create(10)

    uf.union(1, 3)
    uf.union(2, 4)
    uf.union(1, 5)

    print(uf.connected(1, 3))
    print(uf.connected(3, 5))
    print(uf.connected(1, 2))
    print(uf.connected(1, 4))

