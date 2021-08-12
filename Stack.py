from LinkedList import *


class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def is_empty(self):
        return self.stack.is_empty()

    def push(self, element):
        self.stack.insert_first(element)

    def pop(self):
        return self.stack.delete_first()

    def print_stack(self):
        self.stack.print_list()


class StackByList:
    """ Using Python built-in list functions are a bit
    more expensive than using the LinkedList class """
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def print_stack(self):
        print(self.stack)


def use_stack():
    s = StackByList()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.print_stack()
    s.pop()
    s.pop()
    s.print_stack()
    print(s.is_empty())
    while not s.is_empty():
        s.pop()
    print(s.is_empty())
    s.print_stack()


if __name__ == '__main__':
    use_stack()
