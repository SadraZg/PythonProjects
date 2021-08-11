class Node:
    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node


class LinkedList:
    """ LinkedLists have efficiency when dealing with pushing and popping Whereas Python
    built-in lists are efficient when dealing with accessing a specific element.
    In other words, adding to or removing from a LinkedList is efficient but traversing it is not. """
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def insert_first(self, element):
        n = Node(element, self.head)
        if self.head is None:
            self.head = self.tail = n
        else:
            n.next_node = self.head
            self.head = n

    def insert_last(self, element):
        n = Node(element)
        if self.head is None:
            self.head = self.tail = n
        else:
            self.tail.next_node = n
            self.tail = n

    def delete_first(self):
        n = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = n.next_node
            n.next_node = None
        return n.element

    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head
        while current is not None:
            next = current.next_node
            current.next_node = prev
            prev = current
            current = next
        self.head = prev

    def print_list(self):
        n = self.head
        print('[', end=' ')
        while n is not None:
            print(n.element, end=' ')
            n = n.next_node
        print(']')


if __name__ == '__main__':
    LinkedList()
    ll = LinkedList()
    print(ll.is_empty())
    ll.insert_first(7)
    ll.insert_first(5)
    ll.insert_first(3)
    ll.insert_last(9)
    ll.insert_first(1)
    ll.print_list()
    ll.delete_first()
    ll.print_list()
    # while not ll.is_empty():
    #     ll.delete_first()
    ll.reverse()
    ll.print_list()
