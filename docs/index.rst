pyalgs
==========

pyalgs is a library of python implementation for algorithms in the "Algorithms" book (http://algs4.cs.princeton.edu/home/) and Robert Sedgwick's Algorithms course using Python (Part I and Part II)

The main purpose of this library is to provide a companion library for python developers who are learning the algorithms in the "Algorithms" book

Installation:
-------------

To install the package using pip:

::

    $ pip install pyalgs



Usage
-----

To use the algorithms or data structures in your python code:

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

Features
--------

- Algorithms and data structures introduced in the "Algorithms" book.
- Test coverage for each algorithm and data structure.


Tests:
------

the unit tests of all algorithms and data structures can be run with the following command from the root folder:

.. code-block:: bash

    $ python -m unittest discover -s . -p "*_unit_test.py"


Contributing:
-------------

Contributions are always welcome. Check out the contributing guidelines to get
started.

.. _`docs`: http://pyalgs.readthedocs.org/en/latest/
.. _`documentation`: http://pyalgs.readthedocs.org/en/latest/

Table of Contents:
------------------

.. toctree::
   :maxdepth: 2

   pyalgs