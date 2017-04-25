from pyalgs.data_structures.commons.stack import Stack


class Bag(object):
    def __init__(self):
        self.stack = Stack.create()

    def add(self, item):
        self.stack.push(item)

    def size(self):
        return self.stack.size()

    def is_empty(self):
        return self.stack.is_empty()

    def iterate(self):
        return self.stack.iterate()

    @staticmethod
    def create():
        return Bag()
