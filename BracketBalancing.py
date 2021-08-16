class Node:
    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.stack = None

    def push(self, element):
        self.stack = Node(element, self.stack)

    def pop(self):
        element = self.stack.element
        self.stack = self.stack.next_node
        return element

    def is_empty(self):
        return self.stack is None


def balancing_bracket(s):
    stack = Stack()
    for c in s:
        if c in '([{':
            stack.push(c)
        elif c in ')]}':
            if stack.is_empty():
                return False
            popped = stack.pop()
            if popped == '(' and c == ')':
                continue
            elif popped == '[' and c == ']':
                continue
            elif popped == '{' and c == '}':
                continue
            else:
                return False

    return stack.is_empty()


print(balancing_bracket('is(all{fine[ha]})'))
