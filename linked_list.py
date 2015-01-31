__author__ = 'Shane'


class LinkedList:
    """A doubly linked list."""

    def __init__(self):
        self.head = self.tail = None

    def __len__(self):
        length = 0
        n = self.head

        while n:
            length += 1
            n = n['next']

        return length

    def __contains__(self, item):
        n = self.head

        while n:
            if n['value'] == item:
                return True

            n = n['next']

        return False

    def add_to_tail(self, val):
        if not self.tail:
            self.head = self.tail = self.__make_node(val)
        else:
            node = self.__make_node(val, self.tail)
            self.tail.next = node
            self.tail = node

    def add_to_head(self, val):
        if not self.head:
            self.head = self.tail = self.__make_node(val)
        else:
            node = self.__make_node(val, None, self.head)
            self.head.prev = node
            self.head = node

    def remove_from_tail(self):
        if not self.tail:
            return None
        else:
            prev = self.tail.prev
            prev.next = None
            self.tail = prev

    def remove_from_head(self):
        if not self.head:
            return None
        else:
            next = self.head.next
            next.prev = None
            self.head = next

    def __make_node(self, val, prev=None, next=None):
        return {
            'next': next,
            'prev': prev,
            'value': val
        }
