from LinkedList import *


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def is_empty(self):
        return self.queue.is_empty()

    def enqueue(self, element):
        self.queue.insert_last(element)

    def dequeue(self):
        return self.queue.delete_first()

    def print_queue(self):
        self.queue.print_list()


class QueueByList:
    """ Using Python built-in list functions are a bit
        more expensive than using the LinkedList class """
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def enqueue(self, element):
        self.queue.insert(0, element)

    def dequeue(self):
        return self.queue.pop()

    def print_queue(self):
        print(self.queue)


def use_queue():
    q = QueueByList()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.print_queue()
    q.dequeue()
    q.dequeue()
    q.print_queue()
    print(q.is_empty())
    while not q.is_empty():
        q.dequeue()
    print(q.is_empty())
    q.print_queue()


if __name__ == '__main__':
    use_queue()
