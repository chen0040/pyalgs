pyalgs
======

Package pyalgs implements algorithms in the "Algorithms" book (http://algs4.cs.princeton.edu/home/) and Robert Sedgwick's Algorithms course using Python (Part I and Part II)

.. image:: https://travis-ci.org/chen0040/pyalgs.svg?branch=master
    :target: https://travis-ci.org/chen0040/pyalgs

.. image:: https://coveralls.io/repos/github/chen0040/pyalgs/badge.svg?branch=master
    :target: https://coveralls.io/github/chen0040/pyalgs?branch=master

.. image:: https://readthedocs.org/projects/pyalgs/badge/?version=latest
    :target: http://pyalgs.readthedocs.org/en/latest/?badge=latest

.. image:: https://scrutinizer-ci.com/g/chen0040/pyalgs/badges/quality-score.png?b=master
    :target: https://scrutinizer-ci.com/g/chen0040/pyalgs/?branch=master


More details are provided in the `docs`_ for implementation, complexities and further info.

Install pyalgs
==============

Run the following command to install pyalgs using pip

.. code-block:: bash

    $ pip install pyalgs

Features:
=========

* Data Structure
  - Stack
    + Linked List
    + Array
  - Queue
    + Linked List
    + Array
  - Bag
  - HashSet
  - HashMap
    + Separate Chaining
    + Linear Probing
  - Binary Search Tree
  - Red Black Tree
  - Priority Queue
    + MinPQ
    + MaxPQ
    + IndexMinPQ
  - Graph
    + Simple graph
    + Edge weighted graph
    + Directed graph (digraph)
    + Directed edge weight graph
* Algorithms
  - Sorting
    + Selection Sort
    + Insertion Sort
    + Shell Sort
    + Merge Sort
    + Quick Sort
    + 3-Ways Quick Sort
    + Heap Sort
  - Selection
    + Binary Search
  - Shuffling
    + Knuth
  - Union Find
    + Quick Find
    + Weighted Quick Union with path compression
* Graph Algorithms
  - Search
    + Depth First Search
    + Breadth First Search
  - Connectivity
    + Connected Components
    + Strongly Connected Components
  - Topological Sorting
    + Depth First Reverse Post Order
  - Minimum Spanning Tree
    + Kruskal
    + Prim (Lazy)
    + Prim (Eager)

Usage:
======

Data Structure
--------------

Stack


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



Queue


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



Bag


.. code-block:: python

    from pyalgs.data_structures.commons.bag import Bag

    bag = Bag.create()

    bag.add(10)
    bag.add(20)
    bag.add(30)

    print [i for i in bag.iterate()]

    print bag.size()
    print bag.is_empty()


Minimum Priority Queue

.. code-block:: python

    from pyalgs.data_structures.commons.priority_queue import MinPQ

    pq = MinPQ.create()
    pq.enqueue(10)
    pq.enqueue(5)
    pq.enqueue(12)
    pq.enqueue(14)
    pq.enqueue(2)

    print pq.is_empty()
    print pq.size()

    print [i for i in pq.iterate()]

    deleted = pq.del_min()
    print(deleted)


Maximum Priority Queue


.. code-block:: python

    from pyalgs.data_structures.commons.priority_queue import MaxPQ

    pq = MaxPQ.create()
    pq.enqueue(10)
    pq.enqueue(5)
    pq.enqueue(12)
    pq.enqueue(14)
    pq.enqueue(2)

    print pq.is_empty()
    print pq.size()

    print [i for i in pq.iterate()]

    deleted = pq.del_max()
    print deleted


Symbol Table using Binary Search Tree


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


Undirected Graph


.. code-block:: python

    from pyalgs.data_structures.graphs.graph import Graph
    def create_graph():
        G = Graph(100)

        G.add_edge(1, 2)
        G.add_edge(1, 3)

        print([i for i in G.adj(1)])
        print([i for i in G.adj(2)])
        print([i for i in G.adj(3)])

        print(G.vertex_count())
        return G


Directed Graph


.. code-block:: python

    from pyalgs.data_structures.graphs.graph import Digraph
    def create_digraph():
        G = Digraph(100)

        G.add_edge(1, 2)
        G.add_edge(1, 3)

        print([i for i in G.adj(1)])
        print([i for i in G.adj(2)])
        print([i for i in G.adj(3)])

        print(G.vertex_count())
        return G

Edge Weighted Graph

.. code-block:: python

    from pyalgs.data_structures.graphs.graph import EdgeWeightGraph
    def create_edge_weighted_graph():
        g = EdgeWeightedGraph(8)
        g.add_edge(Edge(0, 7, 0.16))
        g.add_edge(Edge(2, 3, 0.17))
        g.add_edge(Edge(1, 7, 0.19))
        g.add_edge(Edge(0, 2, 0.26))
        g.add_edge(Edge(5, 7, 0.28))

        print([edge for edge in G.adj(3)])

        print(G.vertex_count())
        print(', '.join([edge for edge in G.edges()]))
        return g

Algorithms
----------

Union Find


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


Sorting


The sorting algorithms sort an array in ascending order

Selection Sort

.. code-block:: python

    from pyalgs.algorithms.commons.sorting import SelectionSort

    a = [4, 2, 1]
    SelectionSort.sort(a)
    print(a)


Insertion Sort

.. code-block:: python

    from pyalgs.algorithms.commons.sorting import InsertionSort

    a = [4, 2, 1]
    InsertionSort.sort(a)
    print(a)


Shell Sort

.. code-block:: python

    from pyalgs.algorithms.commons.sorting import ShellSort

    a = [4, 2, 1, 23, 4, 5, 6, 7, 8, 9, 20, 11, 13, 34, 66]
    ShellSort.sort(a)
    print(a)


Merge Sort

.. code-block:: python

    from pyalgs.algorithms.commons.sorting import MergeSort

    a = [4, 2, 1, 23, 4, 5, 6, 7, 8, 9, 20, 11, 13, 34, 66]
    MergeSort.sort(a)
    print(a)


Quick Sort

.. code-block:: python

    from pyalgs.algorithms.commons.sorting import QuickSort

    a = [4, 2, 1, 23, 4, 5, 6, 7, 8, 9, 20, 11, 13, 34, 66]
    QuickSort.sort(a)
    print(a)


3-Ways Quick Sort

.. code-block:: python

    from pyalgs.algorithms.commons.sorting import ThreeWayQuickSort

    a = [4, 2, 1, 23, 4, 5, 6, 7, 8, 9, 20, 11, 13, 34, 66]
    ThreeWayQuickSort.sort(a)
    print(a)


Heap Sort

.. code-block:: python

    from pyalgs.algorithms.commons.sorting import HeapSort

    a = [4, 2, 1, 23, 4, 5, 6, 7, 8, 9, 20, 11, 13, 34, 66]
    HeapSort.sort(a)
    print(a)



Selection


Binary Selection

.. code-block:: python

    from pyalgs.algorithms.commons.selecting import BinarySelection
    from pyalgs.algorithms.commons.util import is_sorted


    a = [1, 2, 13, 22, 123]
    assert is_sorted(a)
    print BinarySelection.index_of(a, 13)


Shuffle


Knuth Shuffle

.. code-block:: python

    from pyalgs.algorithms.commons.shuffling import KnuthShuffle

    a = [1, 2, 13, 22, 123]
    KnuthShuffle.shuffle(a)
    print(a)

Graph
-----

Depth First Search

.. code-block:: python

    from pyalgs.algorithms.graphs.search import DepthFirstSearch
    g = create_graph()
    s = 0
    dfs = DepthFirstSearch(g, s)

    for v in range(1, g.vertex_count()):
        if dfs.hasPathTo(v):
            print(str(s) + ' is connected to ' + str(v))
            print('path is ' + ' => '.join([str(i) for i in dfs.pathTo(v)]))

Breadth First Search

.. code-block:: python

    from pyalgs.algorithms.graphs.search import BreadthFirstSearch
    g = create_graph()
    s = 0
    dfs = BreadthFirstSearch(g, s)

    for v in range(1, g.vertex_count()):
        if dfs.hasPathTo(v):
            print(str(s) + ' is connected to ' + str(v))
            print('path is ' + ' => '.join([str(i) for i in dfs.pathTo(v)]))

Connected Components

.. code-block:: python

    from pyalgs.algorithms.graphs.connectivity import ConnectedComponents
    G = create_graph()

    cc = ConnectedComponents(G)
    print('connected component count: ' + str(cc.count()))


    for v in range(G.vertex_count()):
        print('id[' + str(v) + ']: ' + str(cc.id(v)))
    for v in range(G.vertex_count()):
        r = randint(0, G.vertex_count()-1)
        if cc.connected(v, r):
            print(str(v) + ' is connected to ' + str(r))

Topological Sort

.. code-block:: python

    from pyalgs.algorithms.graphs.topological_sort import DepthFirstOrder
    G = create_graph()
    topological_sort = DepthFirstOrder(G)
    print(' => '.join([str(i) for i in topological_sort.postOrder()]))

Minimum Spanning Tree (Kruskal)

.. code-block:: python

    g = create_edge_weighted_graph()
    mst = KruskalMST(g)

    tree = mst.spanning_tree()

    for e in tree:
        print(e)

.. _`docs`: http://pyalgs.readthedocs.org/en/latest/
.. _`documentation`: http://pyalgs.readthedocs.org/en/latest/