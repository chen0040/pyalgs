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

Install pyalgs
--------------

Run the following command to install pyalgs using pip

::

    $ pip install pyalgs


Data Structure
==============

Stack
+++++

::

    from pyalgs.data_structures.commons.stack import Stack

    stack = Stack.create()
    stack.push(10)
    stack.push(1)

    print [i for i in stack.iterate()]

    print stack.is_empty()
    print stack.size()

    popped_item = stack.pop()
    print popped_item



