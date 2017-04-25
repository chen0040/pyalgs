# pyalgs

Package pyalgs implements algorithms in Robert Sedgwick's Coursera course using Python (Part I and Part II)

## Data Structure

### Stack

<pre>
from pyalgs.data_structures.commons.stack import Stack

stack = Stack.create()
stack.push(10)
stack.push(1)

print stack.is_empty()
print stack.size()

popped_item = stack.pop()
print popped_item
</pre>


### Queue

<pre>
from pyalgs.data_structures.commons.queue import Queue

queue = Queue.create()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print queue.size()
print queue.is_empty()

deleted_item = queue.dequeue())
print deleted_item
</pre>

## Algorithms

### Sorting

The sorting algorithms sort an array in ascending order

#### Selection Sort

<pre>
from pyalgs.algorithms.commons.sorting import SelectionSort

a = [4, 2, 1]
SelectionSort.sort(a)
print a
</pre>

#### Insertion Sort

<pre>
from pyalgs.algorithms.commons.sorting import InsertionSort

a = [4, 2, 1]
InsertionSort.sort(a)
print a
</pre>

#### Shell Sort

<pre>
from pyalgs.algorithms.commons.sorting import ShellSort

a = [4, 2, 1, 23, 4, 5, 6, 7, 8, 9, 20, 11, 13, 34, 66]
ShellSort.sort(a)
print a
</pre>

#### Merge Sort

<pre>
from pyalgs.algorithms.commons.sorting import MergeSort

a = [4, 2, 1, 23, 4, 5, 6, 7, 8, 9, 20, 11, 13, 34, 66]
MergeSort.sort(a)
print a
</pre>