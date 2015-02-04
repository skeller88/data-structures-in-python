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

    def __contains__(self, key):
        n = self.head

        while n:
            if n['key'] == key:
                return True

            n = n['next']

        return False

    def add_to_tail(self, key, value=None):
        if not self.tail:
            self.head = self.tail = self.__make_node({
                'key': key, 'value': value
            })
        else:
            node = self.__make_node({
                'key': key,
                'next': None,
                'prev': self.tail,
                'value': value
            })
            self.tail['next'] = node
            self.tail = node

        return self.tail

    def add_to_head(self, key, value=None):
        if not self.head:
            self.head = self.tail = self.__make_node({'key': key})
        else:
            node = self.__make_node({
                'key': key,
                'next': self.head,
                'prev': None,
            })
            self.head['prev'] = node
            self.head = node

        return self.head

    def remove_from_tail(self):
        old_tail = self.tail

        if not self.tail:
            return None
        elif self.tail == self.head:
            self.tail = self.head = None
        else:
            prev = self.tail['prev']
            prev['next'] = None
            self.tail = prev

        return old_tail

    def remove_from_head(self):
        old_head = self.head

        if not self.head:
            return None
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            next = self.head['next']
            next['prev'] = None
            self.head = next

        return old_head

    def __make_node(self, options):
        return {
            'key': options.get('key'),
            'next': options.get('next'),
            'prev': options.get('prev'),
            'value': options.get('value'),
        }

    def update_node(self, key, value):
        """Mainly used by hash table."""
        node = self.head

        while node:
            if node['key'] == key:
                node['value'] = value
                return
            node = node['next']

        raise Exception('No node with key ' + key + ' exists.')

    def remove_node(self, key):
        node = self.head

        while node:
            if node['key'] == key:
                if node == self.head:
                    self.remove_from_head()
                elif node == self.tail:
                    self.remove_from_tail()
                else:
                    node['prev']['next'] = node['next']
                    node['next']['prev'] = node['prev']

                return node

            node = node['next']

        return None

    def get_node_value(self, key):
        node = self.head

        while node:
            if node['key'] == key:
                return node['value']

            node = node['next']

        return None
