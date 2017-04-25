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

#### Selection Sort

<pre>
from pyalgs.algorithms.commons.sorting import SelectionSort

a = [4, 2, 1]
SelectionSort.sort(a)
print a
</pre>